def determine_winner():
    # 점수별 사과 팀의 스코어
    apple_3_pointers = int(input().strip())
    apple_2_pointers = int(input().strip())
    apple_1_pointers = int(input().strip())

    # 사과 팀의 총 스코어
    apples_score = apple_3_pointers * 3 + apple_2_pointers * 2 + apple_1_pointers * 1

    # 점수별 바나나 팀의 스코어
    banana_3_pointers = int(input().strip())
    banana_2_pointers = int(input().strip())
    banana_1_pointers = int(input().strip())

    # 바나나 팀의 총 스코어
    bananas_score = banana_3_pointers * 3 + banana_2_pointers * 2 + banana_1_pointers * 1

    # 게임에서 사과 팀이 이겼는지, 바나나 팀이 이겼는지, 아니면 두 팀이 비겼는지 결정
    if apples_score > bananas_score:
        print('A')
    elif apples_score < bananas_score:
        print('B')
    else:
        print('T')
