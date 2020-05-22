"""Bubble Sort Algorithm on Array"""

def bubble_sort(arr):
    arrLength = len(arr)
    while arrLength > 0:
        for i in range(arrLength-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        arrLength -= 1
    return arr

def main():
    # Create an unsorted array
    my_arr = [3, 4, 1, 2, 5, 8, 0, 100, 17]
    
    # Print the array before and after sorting
    print(f"Before: {my_arr}")
    new_arr = bubble_sort(my_arr)
    print(f"After: {new_arr}")

if __name__ == "__main__":
    main()
