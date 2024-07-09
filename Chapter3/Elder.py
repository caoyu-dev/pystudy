#https://dmoj.ca/problem/coci18c4p1v

# 초기 마법사를 저장할 변수
current_wizard = input()[0]

# 대결의 수를 저장할 변수
n = int(input())

# Elder Wand 를 소유했던 마법사들을 저장할 집합
wizards_set = set()
wizards_set.add(current_wizard)

# 대결 결과를 처리
for _ in range(n):
    duel = input()
    winner = duel[0]
    loser = duel[2]

    # 만약 현재 Elder Wand 를 소유하고 있는 마법사가 패배하는 경우
    if current_wizard == loser:
        # Elder Wand 의 소유자를 승리자로 변경
        current_wizard = winner
        # 새로운 소유자를 집합에 추가
        wizards_set.add(current_wizard)

# 최종 Elder Wand 소유자 출력
print(current_wizard)

# 서로 다른 Elder Wand 소유자 수 출력
print(len(wizards_set))
