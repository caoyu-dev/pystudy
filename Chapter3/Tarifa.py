#https://dmoj.ca/problem/coci16c1p1

def used_megabytes():
    # 값 입력 받기
    X = int(input()) # 매달 사용할 수 있는 메가바이트
    N = int(input()) # 사용할 개월 수

    # 처음에는 사용 가능한 메가바이트는 0으로 시작
    available_mb = 0

    # N개월 동안 사용한 메가바이트 입력 받고 계산
    for i in range(N):
        used_mb = int(input())
        available_mb += (X - used_mb)

    # 마지막 달에 사용할 수 있는 총 메가바이트 출력
    print(available_mb + X)

used_megabytes()
