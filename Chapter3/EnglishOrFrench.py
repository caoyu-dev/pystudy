#https://dmoj.ca/problem/ccc11s1

def is_english_or_french(N, lines):
    t_count = 0  # t 와 T 의 출현 횟수를 저장할 변수
    s_count = 0  # s 와 S 의 출현 횟수를 저장할 변수

    # 주어진 텍스트의 각 줄을 반복 처리
    for line in lines:
        for char in line:
            if char == 't' or char == 'T':
                t_count += 1
            elif char == 's' or char == 'S':
                s_count += 1

    # t 와 s 의 개수를 비교하여 언어 판별
    if t_count > s_count:
        return "English"
    else:
        return "French"

# 값 입력 받기
N = int(input())
lines = []
for _ in range(N):
    line = input()
    lines.append(line)

# 함수를 호출하여 결과를 출력
result = is_english_or_french(N, lines)
print(result)
