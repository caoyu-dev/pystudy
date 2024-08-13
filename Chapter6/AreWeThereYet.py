def calculate_distances(distances):
    # 입력 받은 거리를 통해 누적 거리 계산
    cumulative_distances = [0] * 5
    for i in range(1, 5):
        cumulative_distances[i] = cumulative_distances[i - 1] + distances[i - 1]

    result = []
    for i in range(5):
        row = []
        for j in range(5):
            # 절대값 함수를 사용하여 거리 계산
            distance = abs(cumulative_distances[i] - cumulative_distances[j])
            row.append(str(distance))
        result.append(' '.join(row))

    return result

# 입력
try:
    distances = list(map(int, input().split()))
    if len(distances) != 4:
        raise ValueError("정확히 4개의 거리를 입력해야 합니다.")
except ValueError as e:
    print("입력 오류:", e)
    exit()  # 입력 오류가 발생하면 프로그램 종료

# 결과 계산 및 출력
results = calculate_distances(distances)
for line in results:
    print(line)
