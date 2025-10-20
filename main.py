from qrcodecreator.qr_code_creator import QrCodeCreator

qr_code = QrCodeCreator(1, 10, 4, "https://google.com")
qr_code.create_code()
