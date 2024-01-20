from app import create_app, db
from models import Vendor, Sweet, VendorSweet

# Create the Flask application
app = create_app()

# Use the application context
with app.app_context():
    # Your database-related code here
    insomnia_cookies = Sweet(name='Insomnia Cookies', description='Delicious cookies for late-night cravings')
    cookies_cream = Sweet(name='Cookies and Cream', description='A delightful mix of cookies and cream')
    chocolate_chip_cookie = Sweet(name='Chocolate Chip Cookie', description='Classic chocolate chip goodness')
    brownie = Sweet(name='Brownie', description='Rich and fudgy brownies')

    vendor1 = Vendor(name='Sweet Delights', location='Downtown')
    vendor2 = Vendor(name='Treats Galore', location='Uptown')

    # Associate sweets with vendors
    vendor1.vendor_sweets.extend([VendorSweet(price=2.0, sweet=insomnia_cookies)])
    vendor1.vendor_sweets.extend([VendorSweet(price=2.5, sweet=cookies_cream)])
    
    vendor2.vendor_sweets.extend([VendorSweet(price=1.8, sweet=chocolate_chip_cookie)])
    vendor2.vendor_sweets.extend([VendorSweet(price=3.0, sweet=brownie)])

    # Add sweets and vendors to the database session
    db.session.add_all([insomnia_cookies, cookies_cream, chocolate_chip_cookie, brownie, vendor1, vendor2])

    # Commit the changes to the database
    db.session.commit()
