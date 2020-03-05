from app import db
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from app import ma

# Barcodes are the unique codes found on the back of student IDs

class Barcode(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String, unique=True, nullable=False)
    last_used = db.Column(TIMESTAMP, nullable=True)
    belongs_to = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=True)

    # scan_event_id = db.relationship('ScanEvent')

    # @last_used.expression
    # def last_used(self):
    #     db.select(['Scan'])


class BarcodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Barcode
        include_fk = True