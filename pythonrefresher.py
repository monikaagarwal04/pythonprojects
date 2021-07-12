#--------------------------
name = "julie"
age = 41


print ("Hi my name is {} and I am {} years old".format(name, age)) 

if age > 18:
    print ("you are older than 18")
#--------------------------
#single line comment
"""multi line
    comment
"""
#--------------------------
year = 2001

if year >= 2000 and year <= 2099:
    print ("Welcome to the 21st century!")
else: 
    print ("You are before or after the 21st century")
#--------------------------

def tripleprint(message = "hello"):
    print (message*3)


tripleprint()

#-------------------------

dognames = ['fido', 'reta', 'erem', 'ellisa']

print(dognames)

for dog in dognames:
    print(dog)

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for num in numbers:
    if(num > 90):
        print (num)

#--------------------------

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for x in range(0,2):
    cooldictionary[words[x]] = definitions[x]

print (cooldictionary)

#--------------------------

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        print (2020 - self.year)

#--------------------------

