#https://dmoj.ca/problem/coci06c5p1

def move():
    # 초기 공의 위치는 왼쪽 컵(1번 컵) 아래
    ball_position = 1

    # 움직임을 나타내는 문자열 입력
    moves = input()

    # 움직임 문자열의 각 문자에 대해 공의 위치를 업데이트
    for move in moves:
        if move == 'A':
            if ball_position == 1:
                ball_position = 2
            elif ball_position == 2:
                ball_position = 1
        elif move == 'B':
            if ball_position == 2:
                ball_position = 3
            elif ball_position == 3:
                ball_position = 2
        elif move == 'C':
            if ball_position == 1:
                ball_position = 3
            elif ball_position == 3:
                ball_position = 1

    print(ball_position)

move()
