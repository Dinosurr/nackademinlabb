for i in range(10):
    #    print("Hej")
    times = 1
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in number:
    for i in range(times):
        times += 1
#        print(item)


answer = 42
correct = False

while not correct:
    userInput = int(input("Enter a integer"))
    if userInput == answer:
        print("Correct")
        correct = True
    elif userInput < answer:
        print("Wrong, its higher")
    elif userInput > answer:
        print("Wrong, its lower")