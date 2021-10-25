def print_length(_list):
    print("List length: {}".format(len(_list)))


ab = ["ab"] * 6
twos = [2] * 10
z = ['z'] * 15

myList = ab + twos + z
print("Initial")
print(myList)
print_length(myList)

myList[-1] = 'last'
print("1.")
print(myList)
print_length(myList)

myList[len(myList) // 2] = 'x'
print("2.")
print(myList)
print_length(myList)

myList[1:2] = 'a', 2, 'zz'
print("3.")
print(myList)
print_length(myList)

del myList[3:10]
print("4.")
print(myList)
print_length(myList)

myList.remove(2)
print("5.")
print(myList)
print_length(myList)

myList[2:12] = myList[2:12][::-1]
print("6.")
print(myList)
print_length(myList)

count = 0
for i in myList:
    if i == 2:
        count = count + 1

print("Number of occurrences of two: {}".format(count))
print("Index of the first occurrence: {}".format(myList.index(2)))
