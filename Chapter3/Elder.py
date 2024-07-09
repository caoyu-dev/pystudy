#https://dmoj.ca/problem/coci18c4p1

# 초기 마법사를 저장할 변수
initial_wizard = input()[0]
if len(initial_wizard) != 1 or not ('A' <= initial_wizard <= 'Z'):
    exit("초기 마법사 오류")

# 대결의 수를 저장할 변수
n = input()
if not n.isdigit() or not (1 <= int(n) <= 100):
    exit("결투 수 오류")
n = int(n)

# Elder Wand 를 소유했던 마법사들을 저장할 집합
current_wizard = initial_wizard
wizards_set = set()
wizards_set.add(current_wizard)

# 대결 결과를 처리
for _ in range(n):
    duel = input()
    # duel 이 3 이 아닌 경우, 중간이 ' ' 없는 경우, duel 하는 사람이 A 와 Z 사이에 나타나지 않는 경우, duel 하는 사람이 같은 경우
    if len(duel) != 3 or duel[1] != ' ' or not ('A' <= duel[0] <= 'Z') or not ('A' <= duel[2] <= 'Z') or duel[0] == duel[2]:
        exit("duel 케이스에 문제가 있다")

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
