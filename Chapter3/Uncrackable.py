#https://dmoj.ca/problem/wc17c3j3

def is_valid_password():
    # 값 입력 받기
    password = input()

    # 앞뒤 공백을 수동으로 제거
    start = 0
    end = len(password) - 1

    while start <= end and password[start] == ' ':
        start += 1
    while end >= start and password[end] == ' ':
        end -= 1

    trimmed_password = password[start:end + 1]

    # 초기화
    length = 0
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0

    # 길이 계산
    for char in trimmed_password:
        length += 1
        # 소문자 확인
        if 'a' <= char <= 'z':
            lowercase_count += 1
        # 대문자 확인
        elif 'A' <= char <= 'Z':
            uppercase_count += 1
        # 숫자 확인
        elif '0' <= char <= '9':
            digit_count += 1

    # 유효성 검사
    if 8 <= length <= 12 and lowercase_count >= 3 and uppercase_count >= 2 and digit_count >= 1:
        return "Valid"
    else:
        return "Invalid"

print(is_valid_password())
