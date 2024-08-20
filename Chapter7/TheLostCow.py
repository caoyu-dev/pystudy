def find_distance(x, y):
    # 초기 위치
    current_position = x
    total_distance = 0
    move_distance = 1
    sign = 1

    while True:
        next_position = x + sign * move_distance

        # Bessie 가 이 안에 있으면 현재 Bessie 의 거리까지만 더하고 끝
        if (current_position <= y <= next_position) or (next_position <= y <= current_position):
            total_distance += abs(y - current_position)
            break
        else:
            # Bessie 가 이 안에 없으면 전체 거리를 더하고 끝
            total_distance += abs(next_position - current_position)
            current_position = next_position
            move_distance *= 2
            sign *= -1

    return total_distance

if __name__ == "__main__":
    with open("direction.in", "r") as infile:
        data = infile.read().splitlines()

    for line in data:
        x, y = map(int, line.split())
        print(find_distance(x, y))

