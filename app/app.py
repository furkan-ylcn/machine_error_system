import sys
import os
from flask import Flask, render_template, request, jsonify, send_file

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from qrcodeoperations.qr_code_creator import QrCodeCreator
from db.models.qr_code import QrCode
import urllib.parse
from mongoengine import connect
import io
import base64

app = Flask(__name__)

with open('./db/db_password.txt', 'r') as f:
    password = f.read().strip()
    
password = urllib.parse.quote(password)

uri = (
    "mongodb+srv://furkanyalcin07_db_user:"
    f"{password}@ek-mes.qsfrqrz.mongodb.net/"
    "qr_codes_db?retryWrites=true&w=majority&appName=EK-MES"
)

try:
    connect(
        db='qr_codes_db',
        host=uri,
        alias='default'
    )
    print("Connected to MongoDB")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

@app.route('/')
def homepage():
    return render_template('index.html', title="EK Machine Error System", year="2025")

@app.route('/create-qrcode', methods=['POST'])
def create_qrcode():
    try:
        machine_number = int(request.json.get('machine_number'))
        
        existing_qr = QrCode.objects(machine_number=machine_number).first()
        
        if existing_qr:
            return jsonify({
                'success': False, 
                'message': f'Machine number {machine_number} already exists'
            })
        
        # Create new QR code
        qr_code_obj = QrCodeCreator(version=1, boxsize=10, border=4, machine_number=machine_number)
        qr_code_obj.create_code()
        
        return jsonify({
            'success': True, 
            'message': f'QR code for machine {machine_number} created successfully'
        })
        
    except ValueError:
        return jsonify({
            'success': False, 
            'message': 'Invalid machine number'
        })
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Error creating QR code: {str(e)}'
        })

@app.route('/qrcode/<int:machine_number>')
def get_qrcode(machine_number):
    try:
        qr_code = QrCode.objects(machine_number=machine_number).first()
        
        if not qr_code:
            return "QR code not found", 404
        
        if hasattr(qr_code.binary, 'decode'):
            image_data = base64.b64decode(qr_code.binary)
        else:
            image_data = base64.b64decode(qr_code.binary)
        
        img_io = io.BytesIO(image_data)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
        
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)