from app import db

# Barcodes are the unique codes found on the back of student IDs

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String, unique=True, nullable=False)
    lastUsed = db.Column(db.DATETIME, nullable=True)
    Description = db.Column(db.String, nullable=False)
    Query = db.Column(db.JSON, nullable=False)
