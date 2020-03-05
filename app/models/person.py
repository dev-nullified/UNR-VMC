# from app import db, ma
from .. import db, ma


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nsheid = db.Column(db.BigInteger)
    netid = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    middle_initial = db.Column(db.String)
    email_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    age = db.Column(db.Integer)
    # gender = db.Column(db.String)
    # ethnicity = db.Column(db.String)
    # nshe_residency_status = db.Column(db.Boolean) #True is "IS" which is in state, # False is "OS" which is out of state
    # currently_live_on_campus = db.Column(db.Boolean)
    # how_far_from_unr = db.Column(db.Boolean) # if currently_live_on_campus is true then how far do they live from unr


    avatar_path = db.Column(db.String)  # User's photo

    # Address specific (based on the xNAL Name and address Standard)

    postal_code = db.Column(db.String)  # i.e. Zip Code
    street = db.Column(db.String)  # i.e. Street address
    state = db.Column(db.String)  # i.e. State (Stores ISO code)
    city = db.Column(db.String)  # i.e. City (Stores ISO code)
    address2 = db.Column(db.String)  # i.e. Apartment, Suite, Box number, etc.




    # Relationship
    # barcodes = db.relationship('Barcode', backref='person', lazy=True)



#   Academic Info
#     academic_career = db.Column(db.String)
#     academic_level = db.Column(db.String)
#     academic_load_full_time = db.Column(db.Boolean) #Full time is TRUE, Part time is FALSE
#     academic_unit_taken = db.Column(db.Integer)
#     academic_status = db.Column(db.String)
#
# #   Scholarship info
#     stem_scholarship = db.Column(db.Boolean)
#
# #   Other
#     gi_benefit_chapter = db.Column(db.String)



# Alias table
# EmployeeID = NSHE ID
# STRM = Student term
# EXT_TYPE = ?
# ACAD_CAREER

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        include_fk = True
        load_instance = False