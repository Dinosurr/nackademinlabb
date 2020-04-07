# userA = input("Name for user A")
# userB = input("Name for user B")
# userC = input("Name for user C")
# people = {userA: [input("age a"), input("shoesize a")],
#          userB: [input("age b"), input("shoesize b")],
#          userC: [input("age c"), input("shoesize c")]
#          }
userA = [input("name A"), input("age"), input("shoe")]
userB = [input("name B"), input("age"), input("shoe")]
userC = [input("name C"), input("age"), input("shoe")]

ages = [userA, userB, userC]
ages.sort(reverse=True)

print("The oldest is:", ages[0][0], "with shoesize:", ages[0][-1])

ages.sort(key=lambda x: x[2])
print(ages[1][0], "has the median shosize and is", ages[1][1], "years old")



print(ages)





