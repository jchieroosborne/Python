#five names from the user and store them in a list
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

#Bubble Sort to sort the list in ascending order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #if any swaps were made in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        #If no elements were swapped, the list is already sorted
        if not swapped:
            break

#Sort the names using Bubble Sort
bubble_sort(names)

#Print the sorted list
print("Sorted list of names:")
print(names)

#Reverse the sorted list using a Python list method
names.reverse()

#Print the final reversed list
print("Reversed list of names:")
print(names)
