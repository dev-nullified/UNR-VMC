from app import db
from sqlalchemy.dialects.postgresql import TIMESTAMP


class ScanEvent(db.Model):

    id = db.Column(db.BigInteger, primary_key=True)
    scan_date = db.Column(TIMESTAMP, nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('EventType.id'))
    barcode_id = db.Column(db.Integer, db.ForeignKey('BarCode.id'))


class EventType(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String)

    scan_event = db.relationship("ScanEvent")
