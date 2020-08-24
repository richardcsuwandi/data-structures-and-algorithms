def hanoi(from_rod, to_rod, help_rod, n):
    if n==1:
        print("Move from",from_rod,"to",to_rod)
    else:
        hanoi(from_rod, help_rod, to_rod, n-1)
        print("Move from",from_rod,"to",to_rod)
        hanoi(help_rod, to_rod, from_rod, n-1)

if __name__ == "__main__":
    hanoi("left", "right", "middle", 3)