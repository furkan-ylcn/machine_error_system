import qrcode
import random
import os

class QrCodeCreator:
    def __init__(self, version, boxsize, border, data):
        self.version = version
        self.boxsize = boxsize
        self.border = border
        self.data = data

    def create_code(self):
        id = random.random() * 1000
        
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.boxsize,
            border = self.border
        )

        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        folder_path = "./qrcodes"

        for filename in os.listdir(folder_path):
            id = int(random.random() * 1000)
            
            if filename != 'code' + str(id) + '.png':
                img.save("./qrcodes/code" + str(id) + ".png")
                break

        # img.save('./qrcodes/code2.png')
