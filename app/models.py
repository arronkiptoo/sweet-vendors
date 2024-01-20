from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', backref='vendor', lazy=True)

class Sweet(db.Model):
    __tablename__ = 'sweet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', backref='sweet', lazy=True)

class VendorSweet(db.Model):
    __tablename__ = 'vendor_sweet'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    @validates('price')
    def validate_price(self, key, value):
        if not value:
            raise ValueError("Price cannot be blank.")
        elif value < 0:
            raise ValueError("Price cannot be a negative number.")
        return value

    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
