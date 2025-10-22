from io import BytesIO

class QRBinaryConverter:
    def __init__(self, qr_code_image):
        self.qr_code_image = qr_code_image

    def convert_to_binary(self):
        buffer = BytesIO()
        self.qr_code_image.save(buffer, format="PNG")
        qr_binary = buffer.getvalue()
        return qr_binary