fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
myBasket = []
basketRoom = int(input("How much does your basket fit"))
fruitsUsed = 0

while fruitsUsed < basketRoom:
    for i in range(basketRoom):
        for item in fruits:
            myBasket.append(item)
            fruitsUsed += 1
print(myBasket)