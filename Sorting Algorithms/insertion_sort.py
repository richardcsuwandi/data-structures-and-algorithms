def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i-1 >= 0 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1         
    return arr

def main():
    # Create an unsorted array
    my_arr = [5, 1, 4, 3, 6, 7, 2, 9, 8]

    # Print the array before and after sorting
    print(f"Before: {my_arr}")
    new_arr = insertion_sort(my_arr)
    print(f"After: {new_arr}")

if __name__ == "__main__":
    main()
