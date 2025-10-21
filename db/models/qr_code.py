from mongoengine import Document

class QrCode(Document):
    machine_number = IntField(required=True)
    binary = IntField(required=True)