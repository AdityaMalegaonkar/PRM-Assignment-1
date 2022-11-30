lst = []
size = int(input("Enter the number of elements you want to enter in the list : "))
for i in range(size):
    element = input("Enter the element :")
    lst.append(element)
lst.sort(key=lambda x : x[-2])
print("\nSorted List\n")
print(lst)