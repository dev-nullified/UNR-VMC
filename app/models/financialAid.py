from app import db


class FinancialAid(db.model):

    id = db.Column(db.Integer, primary_key=True)
    grant_name = db.Column(db.String)
    status = db.Column(db.Bool)  # Null is not sure, True is yes, False is no
    dateChaned =

    barcodes = db.relationship('Barcode', backref='person', lazy=True)