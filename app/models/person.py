from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nsheid = db.Column(db.Integer)
    netid = db.Column(db.String)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    middelInitial = db.Column(db.String)
    emailaddress = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

    avatarPath = db.Column(db.String)  # User's photo

    # Address specific (based on the xNAL Name and address Standard)

    postalCode = db.Column(db.String)  # i.e. Zip Code
    thoroughfare = db.Column(db.String)  # i.e. Street address
    administrativeArea = db.Column(db.String)  # i.e. State (Stores ISO code)
    locality = db.Column(db.String)  # i.e. City (Stores ISO code)
    premise = db.Column(db.String)  # i.e. Apartment, Suite, Box number, etc.

    # Relationship
    barcodes = db.relationship('Barcode', backref='person', lazy=True)
