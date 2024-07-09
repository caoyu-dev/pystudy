#https://dmoj.ca/problem/ccc18j2

def count_occupied_spaces():
    # 값 입력 받기
    n = int(input())
    yesterday = input()
    today = input()

    # 어제와 오늘 모두 차가 주차된 공간의 수를 세기 위한 변수
    occupied_both_days = 0

    # 두 문자열을 순회하며 비교
    for i in range(n):
        if yesterday[i] == 'C' and today[i] == 'C':
            occupied_both_days += 1

    print(occupied_both_days)

occupy()
