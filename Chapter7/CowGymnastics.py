def count_consistent_pairs(K, N, rankings):
    consistent_pairs = 0

    # 모든 (i, j) 확인
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue

            # i > j 인지 확인
            is_consistent = True
            for session in rankings:
                if session.index(i) > session.index(j):
                    is_consistent = False
                    break

            if is_consistent:
                consistent_pairs += 1

    return consistent_pairs

if __name__ == "__main__":
    with open("gymnastics.in", "r") as infile:
        K, N = map(int, infile.readline().split())
        rankings = [list(map(int, infile.readline().split())) for _ in range(K)]

    result = count_consistent_pairs(K, N, rankings)

    with open("gymnastics.out", "w") as outfile:
        outfile.write(f"{result}\n")
