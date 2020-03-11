from app import db


class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    last_used = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String, nullable=False)

    # Conditions
    conditions = db.Column(db.json, nullable=True)

    #Column mappin gand order for report
    columns = db.relationship("ReportFieldIntersect")
    


class ReportFieldIntersect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    posistion = db.Column(db.integer, nullable=False)

    # One to many, this being the many side
    field_id = db.Column(Integer, ForeignKey('ReportFields.id'))
    report_id = db.Column(Integer, ForeignKey('Reports.id'))

class ReportFields(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias_name = db.Column(db.String, nullable=False)
    report = db.relationship("ReportFieldIntersect")


