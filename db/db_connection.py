from mongoengine import connect
from pymongo.server_api import ServerApi
import urllib.parse

class ConnectDB:
    @staticmethod
    def connect():
        with open('./db/db_password.txt', 'r') as f:
            password = f.read().strip()
        
        password = urllib.parse.quote(password)
        
        uri = (
            "mongodb+srv://furkanyalcin07_db_user:"
            f"{password}@ek-mes.qsfrqrz.mongodb.net/"
            "?retryWrites=true&w=majority&appName=EK-MES"
        )
        
        connect(
            db='qr_codes_db',
            host=uri,
            server_api=ServerApi('1')
        )
        print("Connected to MongoDB")