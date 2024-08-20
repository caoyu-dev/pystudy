#https://usaco.org/index.php?page=viewproblem2&cpid=915

def sleepy_cow_herding(positions):
    positions.sort() # 초기 위치
    a, b, c = positions # 소의 위치

    if c == a + 2:
        min_moves = 0
    elif b == a + 2 or c == b + 2:
        min_moves = 1
    else:
        min_moves = 2

    max_moves = max(b - a, c - b) - 1

    return min_moves, max_moves

def main():
    with open("herding.in", "r") as infile:
        positions = list(map(int, infile.readline().strip().split()))

    min_moves, max_moves = sleepy_cow_herding(positions)

    with open("herding.out", "w") as outfile:
        outfile.write(f"{min_moves}\n")
        outfile.write(f"{max_moves}\n")

if __name__ == "__main__":
    main()
