from . import db


class Book(db.Model):
    """Data model for books"""

    __tablename__ = 'books'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)


    @staticmethod
    def from_dict(dict):
        return Book(name=dict['name'])

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'name': self.name,
       }