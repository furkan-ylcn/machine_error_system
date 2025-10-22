from qrcodeoperations.qr_code_creator import QrCodeCreator
from db.db_connection import ConnectDB
from db.models.qr_code import QrCode

ConnectDB.connect()

qr_code_obj = QrCodeCreator(version=1, boxsize=10, border=4, machine_number=5)
qr_code_obj.create_code()