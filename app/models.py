from app import db

class CharacterMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(1), index=True, unique=True)
#TODO: Remove color as Integer?  Hex is easier to work with.
    color = db.Column(db.Integer, index=False, unique=False)
    colorHex = db.Column(db.String(6), index=False, unique=False)
    count = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<CharacterMetadata %r>' % (self.character)
