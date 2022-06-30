from app.extensions import db


class Hotel(db.Model):
    __tablename__ = 'hotels'
     
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    continent_name = db.Column(db.String(100))
    city_name = db.Column(db.String(100))
    country_name = db.Column(db.String(100))
    price = db.Column(db.Float)
    rating = db.Column(db.Float)
    reviews_count = db.Column(db.Integer)
    info_1 = db.Column(db.String(100))
    info_2 = db.Column(db.String(100))
    info_3 = db.Column(db.String(100))
    info_4 = db.Column(db.String(100))
    info_5 = db.Column(db.String(100))
    info_6 = db.Column(db.String(100))
    info_7 = db.Column(db.String(100))

    @classmethod
    def get_by_id(cls, hotel_id):
        return cls.query.filter_by(id=hotel_id).first()

    @classmethod
    def get_by_continent(cls, continent):
        return cls.query.filter_by(continent_name=continent).all()

    @classmethod
    def get_by_country(cls, country):
        return cls.query.filter_by(country_name=country).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()