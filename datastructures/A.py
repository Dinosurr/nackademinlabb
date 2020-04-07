X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
             "Bella": "Klockgatan 1",
             "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW", "Volvo", "Opel", "BMW"]
cars_2 = cars
cars_3 = "????"
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 6}

addresses["Daniel"] = "Prinsgränd 2"

addressesLength = len(addresses)
print(addressesLength)

bellaAddress = addresses["Bella"]
print(bellaAddress)

sortedLast = sorted(addresses.items())
print(sortedLast[-1][1])

addresses: addresses = {v:k for k, v in addresses.items()}
sortedFirst = sorted(addresses.items())
print(sortedFirst[0][1])

cars.sort()
print(cars[0])

saab = "Saab"
cars.append(saab)
print(cars_3)

carSet = list(set(cars))
print(carSet)

numbers = numbers2 & numbers1
print(numbers)
numbersUnion = numbers1 | numbers2
print(numbersUnion)
numbersDiff = numbers1 - numbers2
print(numbersDiff)
