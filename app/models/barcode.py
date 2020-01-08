from app import db

# Barcodes are the unique codes found on the back of student IDs

class Barcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String, unique=True, nullable=False)
    lastUsed = db.Column(db.DATETIME, nullable=True)
    belongsTo = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True)
