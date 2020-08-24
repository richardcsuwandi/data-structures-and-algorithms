def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_lower = []
        items_greater = []
        for item in arr:
            if item < pivot:
                items_lower.append(item)
            else:
                items_greater.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def main():
    # Create an unsorted array
    my_arr = [29, 99, 27, 41, 66, 28, 44, 78, 84]

    # Print the array before and after sorting
    print(f'Before: {my_arr}')
    new_arr = quick_sort(my_arr)
    print(f'After: {new_arr}')

if __name__ == "__main__":
    main()
