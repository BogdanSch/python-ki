def print_collatz(n: int) -> None:
    current = n
    while current != 1:
        print(current)
        if current % 2 == 0:
            current /= 2
        else:
            current = current * 3 + 1

def collatz_length(n: int):
    count = 0
    current = n
    while current != 1:
        if current % 2 == 0:
            current /= 2
        else:
            current = current * 3 + 1
        count += 1

if __name__ == "__main__":
    n = int(input())
    