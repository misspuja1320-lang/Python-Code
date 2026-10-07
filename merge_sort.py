# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Divide the array
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Main program
n = int(input("Enter the number of rows: "))
arr = []
for i in range(0, n):
    p = int(input("Enter the value: "))
    arr.append(p)
print("Original list:",arr)

merge_sort(arr)

print("After sorting:", arr)