def binarySum(list_, start, stop):
    if start >= stop:
        return 0
    elif stop == start + 1:
        return list_[start]
    else:
        mid = (start+stop)//2
        return binarySum(list_, start, mid) + binarySum(list_, mid, stop)

def main():
    list_ = [1, 2, 3, 4, 5, 6, 7]
    print(binarySum(list_, 0, len(list_)))

if __name__ == "__main__":
    main()