"""Buble sort"""
unsorted=[]
num=int(input("Number of elements on array"))

for i in range(num):
    x=input("Add this to the array:")
    unsorted.append(int(x))


    """Sorting them"""
for k in range(num):
    for i in range(num-1):
        if (unsorted[i] > unsorted[i + 1]):
            """x[0], x[1] = x[1], x[0]  swapping elements"""
            unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]

"""Printing the sorted list"""
print("after sorting")
for i in unsorted:
    print(i)