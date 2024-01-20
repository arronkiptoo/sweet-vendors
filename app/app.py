#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Vendor, Sweet, VendorSweet

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  return app

app = create_app()
migrate = Migrate(app, db)


# Routes

@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    vendors_data = [{'id': vendor.id, 'name': vendor.name} for vendor in vendors]
    return jsonify(vendors_data)

@app.route('/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor:
        vendor_data = {'id': vendor.id, 'name': vendor.name,
                       'vendor_sweets': [{'id': vs.id, 'name': vs.sweet.name, 'price': vs.price}
                                         for vs in vendor.vendor_sweets]}
        return jsonify(vendor_data)
    else:
        return jsonify({'error': 'Vendor not found'}), 404

@app.route('/sweets', methods=['GET'])
def get_sweets():
    sweets = Sweet.query.all()
    sweets_data = [{'id': sweet.id, 'name': sweet.name} for sweet in sweets]
    return jsonify(sweets_data)

@app.route('/sweets/<int:sweet_id>', methods=['GET'])
def get_sweet(sweet_id):
    sweet = Sweet.query.get(sweet_id)
    if sweet:
        sweet_data = {'id': sweet.id, 'name': sweet.name}
        return jsonify(sweet_data)
    else:
        return jsonify({'error': 'Sweet not found'}), 404

@app.route('/vendor_sweets', methods=['POST'])
def create_vendor_sweet():
    data = request.json
    price = data.get('price')
    vendor_id = data.get('vendor_id')
    sweet_id = data.get('sweet_id')

    if not all([price, vendor_id, sweet_id]):
        return jsonify({'errors': ['validation errors']}), 400

    vendor_sweet = VendorSweet(price=price, vendor_id=vendor_id, sweet_id=sweet_id)

    db.session.add(vendor_sweet)
    db.session.commit()

    response_data = {'id': vendor_sweet.id, 'name': vendor_sweet.sweet.name, 'price': vendor_sweet.price}
    return jsonify(response_data)

@app.route('/vendor_sweets/<int:vs_id>', methods=['DELETE'])
def delete_vendor_sweet(vs_id):
    vendor_sweet = VendorSweet.query.get(vs_id)
    if vendor_sweet:
        db.session.delete(vendor_sweet)
        db.session.commit()
        return jsonify({})
    else:
        return jsonify({'error': 'VendorSweet not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)
