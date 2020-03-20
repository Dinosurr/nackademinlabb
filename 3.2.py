expectedStringA = "Jag tYcker om äGg"
expectedStringB = "jAG tYCKER iNTE oM SPAM"

stringA = "Jag tYcker om äGg"
stringB = "inte"
stringC = "SPAM"
stringD = " "


a, b, c = stringA.rsplit(" ", 2)
swapA = a.title()
swapA = swapA.swapcase()
swapB = b.capitalize()
swapB = swapB.swapcase()
swapStringB = stringB.title()
swapStringB = swapStringB.swapcase()


swap = stringD.join([swapA, swapStringB, swapB, stringC])

print(swap)

