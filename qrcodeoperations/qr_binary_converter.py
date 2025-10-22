# from io import BytesIO

# class QRBinaryConverter:
#     def __init__(self, qr_code_image):
#         self.qr_code_image = qr_code_image

#     def convert_to_binary(self):
#         buffer = BytesIO()
#         self.qr_code_image.save(buffer, format="PNG")
#         qr_binary = buffer.getvalue()
#         return qr_binary

import base64
import io

class QRBinaryConverter:
    def __init__(self, img):
        self.img = img
    
    def convert_to_binary(self):
        img_byte_arr = io.BytesIO()
        self.img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        return base64.b64encode(img_byte_arr)