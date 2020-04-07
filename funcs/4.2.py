def sort(listA):
    p = 4
    for i in range(len(listA)):
        print(listA)
        if listA[i] < p:
            listSmaller.append(listA[i])
        else:
            listLarger.append(listLarger[i])
    if len(listSmaller) > 1:
        sort(listSmaller)
    if len(listLarger) > 1:
        sort(listSmaller)
    sorted_list = listSmaller, p, listLarger
    return sorted_list


listSmaller = []
listLarger = []
list1 = [1, 4, 7, 2, 3]

print(sort(list1))
