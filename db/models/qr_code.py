from mongoengine import Document, IntField, BinaryField

class QrCode(Document):
    machine_number = IntField(required=True)
    binary = BinaryField(required=True)