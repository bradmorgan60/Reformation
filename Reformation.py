# This is a program designed to help me work on my OOP skills as well as learn the Reformation Brewery menu

from tkinter import *
root = Tk()


class Reformation:
	def __init__(self, name, beer_type, abv, ibu):
		self.name = name
		self.beer_type = beer_type
		self.abv = abv # alcohol by volume
		self.ibu = ibu # international bitterness unit

	def beer_info(self):
		return "{} is a {} which contains {}% ABV. {} IBU".format(self.name, self.beer_type, self.abv, self.ibu)

class JOGR(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Juicy + Lager = JOGR. This crisp lager is 100% pilsen malts with loads of Mosaic and Citra hops for a refreshing lager with a grapefruit hop burst."

JOGR1 = JOGR('JOGR','juicy lager',4.9, 0)
print(JOGR1.beer_info())
print(JOGR1.interest())
print('--------------------------------------')

class Oren(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Malay for Orange. Fine tuned for low bitterness and soft, balanced sweetness. A touch of milk sugar sets off tropical aroma and flavor"


OREN1 = Oren('Oren','hazy pale ale', 5, 0)
print(OREN1.beer_info())
print(OREN1.interest())
print("--------------------------------------")


class Nolan(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

Nolan1 = Nolan("Nolan the Wanderer - Tallulah Gorge", 'New England IPA', 7.2, 0)
print(Nolan1.beer_info())
print('--------------------------------------')

class Haddy(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Light and refreshing, with citrus notes and a mild, tart finish. Coriander, lemon peel, and wheat malts."


Haddy1 = Haddy('Haddy', 'Belgian White Ale', 4.8, 16)
print(Haddy1.beer_info())
print(Haddy1.interest())
print('--------------------------------------')

class Cadence(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Classified as a Belgian Dubbel. Deep fruit aroma with hints of caramel, figs, and Belgian candi sugar."


Cadence1 = Cadence('Cadence', 'Amber Ale', 6.9, 20)
print(Cadence1.beer_info())
print(Cadence1.interest())
print('--------------------------------------')

class Jude(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Belgian Tripel with a sweet, floral aroma and clean citrus finish. No bitterness (0 IBU)."

Jude1 = Jude('Jude', 'Belgian Tripel', 9.2, 0)
print(Jude1.beer_info())
print(Jude1.interest())
print('---------------------------------------')


class Stark(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "An English inspired porter with light toasty notes, subtle flavors of chocolate and coffee, and a light, crisp finish."


Stark1 = Stark('Stark', 'Toasted Porter', 5.5, 0)
print(Stark1.beer_info())
print(Stark1.interest())
print('--------------------------------------')


class Declaration(Reformation):
	def __init__(self, name, beer_type, abv, ibu):
		super().__init__(name, beer_type, abv, ibu)

	def interest(self):
		return "Heavy, rich, and strong. Coffee taste and very good to drink in the colder months."


Dec1 = Declaration('Declaration', 'Russian Imperial Stout', 9.7, 60)
print(Dec1.beer_info())
print(Dec1.interest())
print('--------------------------------------')

