import qrcode

class QrCodeCreator:
    def __init__(self, version, boxsize, border, data):
        self.version = version
        self.boxsize = boxsize
        self.border = border
        self.data = data

    def create_code(self):
        qr = qrcode.QRCode(
            version = self.version,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = self.boxsize,
            border = self.border
        )

        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('./qrcodes/code2.png')
