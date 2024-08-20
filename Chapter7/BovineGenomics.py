from itertools import combinations

def count_explanatory_sets(N, M, spotty_cows, plain_cows):
    count = 0

    for positions in combinations(range(M), 3):
        spotty_patterns = set()
        plain_patterns = set()

        for cow in spotty_cows:
            pattern = (cow[positions[0]], cow[positions[1]], cow[positions[2]])
            spotty_patterns.add(pattern)

        for cow in plain_cows:
            pattern = (cow[positions[0]], cow[positions[1]], cow[positions[2]])
            plain_patterns.add(pattern)

        if spotty_patterns.isdisjoint(plain_patterns):
            count += 1

    return count

def main():
    with open("cownomics.in", "r") as infile:
        N, M = map(int, infile.readline().strip().split())
        spotty_cows = [infile.readline().strip() for _ in range(N)]
        plain_cows = [infile.readline().strip() for _ in range(N)]

    result = count_explanatory_sets(N, M, spotty_cows, plain_cows)

    with open("cownomics.out", "w") as outfile:
        outfile.write(f"{result}\n")

if __name__ == "__main__":
    main()
