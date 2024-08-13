def has_distinct_digits(year):
    digits = list(str(year))
    # 집합으로 변환하여 중복 제거
    unique_digits = set(digits)
    # 자릿수 == 집합, 즉 중복이 없음
    return len(digits) == len(unique_digits)

def next_distinct_year(start_year):
    year = start_year + 1  # 시작하는 연도 1년 뒤부터 검사
    while not has_distinct_digits(year):
        year += 1
    return year

# 입력 받기
start_year = int(input())

# 다음 중복 없는 연도 출력
print(next_distinct_year(start_year))
