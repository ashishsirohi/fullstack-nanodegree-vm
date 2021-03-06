from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
"""veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
	print veggieBurger.id
	print veggieBurger.price
	print veggieBurger.restaurant.name
	print "\n"
"""

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=10).one() 
print UrbanVeggieBurger.price
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

UrbanVeggieBurger_Updated = session.query(MenuItem).filter_by(id=10).one() 
print UrbanVeggieBurger_Updated.price
