from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=True)
    forecasts = db.relationship('Forecast', backref='forecasts')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.Text, nullable=False)
    forecasts = db.relationship("Forecast", backref="forecasts")

    def __repr__(self):
        return '<City {}>'.format(self.city_name)


class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    forecast_datetime = db.Column(db.DateTime, nullable=False)
    forecast = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Forecast {}>'.format(self.forecast_id)



