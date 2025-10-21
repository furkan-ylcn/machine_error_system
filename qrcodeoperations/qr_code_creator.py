import qrcode
import random
import os

class QrCodeCreator:
    def __init__(self, version, boxsize, border, machine_number):
        self.version = version
        self.boxsize = boxsize
        self.border = border
        self.machine_number = machine_number

    def create_code(self):
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

            folder_path = "qrcodes"
            img.save("./qrcodes/machine" + str(number) + ".png")
