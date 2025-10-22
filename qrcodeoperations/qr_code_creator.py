import qrcode
import random
import os
from qrcodeoperations.qr_binary_converter import QRBinaryConverter
from db.models.qr_code import QrCode
import datetime

class QrCodeCreator:
    def __init__(self, version, boxsize, border, machine_number):
        self.version = version
        self.boxsize = boxsize
        self.border = border
        self.machine_number = machine_number

    def create_code(self):
        # for number in range(1, self.machine_number + 1):
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.boxsize,
            border = self.border
        )

        qr.add_data("machine" + str(self.machine_number))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert QR Code to binary for db
        qr_binary = QRBinaryConverter(img)
        binary_data = qr_binary.convert_to_binary()

        qr_code_model = QrCode(
            machine_number = self.machine_number,
            binary = binary_data,
            created_at = datetime.datetime.now()
        )

        qr_code_model.save()

    def create_many_codes(self):
        for number in range(1, self.machine_number + 1):
            qr = qrcode.QRCode(
                version = self.version,
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                box_size = self.boxsize,
                border = self.border
            )

            qr.add_data("machine" + str(number))
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convert QR Code to binary for db
            qr_binary = QRBinaryConverter(img)
            binary_data = qr_binary.convert_to_binary()

            qr_code_model = QrCode(
                machine_number = number,
                binary = binary_data,
                created_at = datetime.datetime.now()
            )

            qr_code_model.save()
