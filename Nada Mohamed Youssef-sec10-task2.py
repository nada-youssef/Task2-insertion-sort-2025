print(f"""Problem Statement: 
      You are provided with a list of ages, and you need to sort them in ascending order to determine the age ranking in the group.
      List of Ages: [34, 22, 45, 18, 30, 50, 29, 41, 25, 37, 28]""")

ages = [34, 22, 45, 18, 30, 50, 29, 41, 25, 37, 28]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

sorted_ages = insertion_sort(ages)
print("Sorted Ages:", sorted_ages)
