def highlow(arg1):
    if arg1 <= 5:
        for item in range(0, arg1):
            num = str(arg1)
            num = num * arg1
            print(num)
    elif arg1 > 5:
        num = str(arg1)
        num = num * arg1
        print(num)


uInput = int(input("insert number"))

highlow(uInput)