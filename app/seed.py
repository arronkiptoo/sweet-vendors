from app import db, Vendor, Sweet, VendorSweet

# Create vendors
insomnia_cookies = Vendor(name="Insomnia Cookies")
cookies_cream = Vendor(name="Cookies Cream")

# Create sweets
chocolate_chip_cookie = Sweet(name="Chocolate Chip Cookie")
brownie = Sweet(name="Brownie")

# Add vendors and sweets to the database
db.session.add_all([insomnia_cookies, cookies_cream, chocolate_chip_cookie, brownie])
db.session.commit()

# Create vendor sweets
vendor_sweet_1 = VendorSweet(price=200, vendor=insomnia_cookies, sweet=chocolate_chip_cookie)
vendor_sweet_2 = VendorSweet(price=300, vendor=insomnia_cookies, sweet=brownie)
vendor_sweet_3 = VendorSweet(price=250, vendor=cookies_cream, sweet=chocolate_chip_cookie)

# Add vendor sweets to the database
db.session.add_all([vendor_sweet_1, vendor_sweet_2, vendor_sweet_3])
db.session.commit()

print("Seed data added successfully.")
