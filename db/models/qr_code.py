from mongoengine import Document, IntField, BinaryField, DateTimeField

class QrCode(Document):
    machine_number = IntField(required=True)
    binary = BinaryField(required=True)
    created_at = DateTimeField(required=True)