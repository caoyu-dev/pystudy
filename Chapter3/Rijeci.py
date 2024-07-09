#https://dmoj.ca/problem/coci13c3p1

def count_ab(k):
    if not k.isdigit():
        exit("문자열이 숫자로만 이루어져 있지 않음")

    # k 를 정수로 변환
    k = int(k)

    # a 는 A 의 개수, b 는 B 의 개수
    a, b = 1, 0

    # 다음 단계의 A 와 B 의 수 계산
    for _ in range(k):
        current_a = a
        current_b = b
        a = current_b
        b = current_a + current_b

    # k 번째 단계에서의 A 와 B 의 수 출력
    return a, b

# 예를 들어 입력이 10일 때
k = input()
result = count_ab(k)
print(result[0], result[1])
