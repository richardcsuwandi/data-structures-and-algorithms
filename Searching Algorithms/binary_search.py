"""Binary Search Algorithm on Array"""

def binary_search(arr, target, low, high):
    if low > high:
        print('Cannot find the target number!')
    else:
        mid = (low+high)//2
        if target == arr[mid]:
            print(f'The target number is at position {mid}')
        elif target < arr[mid]:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid+1, high)

def main():
    data = [1, 3, 5, 7, 11, 13, 15, 17, 19, 21]
    target = 13
    binary_search(data, target, 0, len(data)-1)

if __name__ == "__main__":
    main()
