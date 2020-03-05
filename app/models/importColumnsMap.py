from app import db


class ColumnMappingFromCSV(db.model):

    id = db.Column(db.Integer, primary_key=True)
    table_name_col_relation = Column(Integer, ForeignKey('parent.id'))
    name_of_col_from_csv =

    auto_generated =



class ColumnDisplayName(db.model):

    db.Column(db.Integer, primary_key=True)
    table_name =
    table_column =
    display_name