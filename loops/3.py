first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]
output = []
output2 = []
for i in second_list:
    location = first_list.index(i)
    output.append(tuple((i, location)))
    output2.append(i, location)
print(output)