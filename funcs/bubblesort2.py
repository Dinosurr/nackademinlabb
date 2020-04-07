def bubblesort(myList):
    for item in range(len(myList)):
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]


numList = [1, 5, 6, 7, 8, 2, 3, 4, 5, 6, 1, 8,
           9, 4, 243, 23, 12, 19, 54, 43]

bubblesort(numList)
print(numList)