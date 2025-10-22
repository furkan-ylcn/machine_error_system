from qrcodeoperations.qr_code_creator import QrCodeCreator
from db.models.qr_code import QrCode
import urllib.parse
from mongoengine import connect

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

# qr_code_obj = QrCodeCreator(version=1, boxsize=10, border=4, machine_number=1)

# existing_qr = QrCode.objects(machine_number=qr_code_obj.machine_number).first()

# if not existing_qr:
#     qr_code_obj.create_code()
#     print("New QR code created")
# else:
#     print(f"Machine number {qr_code_obj.machine_number} already exists")