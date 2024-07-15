#https://dmoj.ca/problem/ccc00s1

def slot_machines(quarters, m1, m2, m3):
    plays = 0
    machine1_count = m1
    machine2_count = m2
    machine3_count = m3

    while quarters > 0:
        # 첫 번째 기계
        plays += 1
        quarters -= 1
        machine1_count += 1
        if machine1_count == 35:
            quarters += 30
            machine1_count = 0

        if quarters == 0:
            break

        # 두 번째 기계
        plays += 1
        quarters -= 1
        machine2_count += 1
        if machine2_count == 100:
            quarters += 60
            machine2_count = 0

        if quarters == 0:
            break

        # 세 번째 기계
        plays += 1
        quarters -= 1
        machine3_count += 1
        if machine3_count == 10:
            quarters += 9
            machine3_count = 0

    return plays

# 입력 받기
quarters = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

# 결과 출력
result = slot_machines(quarters, m1, m2, m3)
print(f"Martha plays {result} times before going broke.")
