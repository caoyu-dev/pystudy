#https://dmoj.ca/problem/ccc08j2

def simulate_c3mp():
    # 초기 플레이리스트 설정
    playlist = ["A", "B", "C", "D", "E"]

    while True:
        # 사용자로부터 버튼 번호 b 와 누를 횟수 n 입력 받기
        b = int(input())
        if not 1 <= b <= 4:
            exit("버튼 번호는 1 과 4 사이에서 형성됩니다.")
        n = int(input())
        if not 1 <= n <= 10:
            exit("누를 횟수는 1 과 10 사이에서 형성됩니다.")

        # 버튼 4 가 눌렸을 때, 플레이리스트 출력하고 프로그램 종료
        if b == 4:
            print(' '.join(playlist))
            break

        # 각 버튼에 따라 플레이리스트 조작
        for _ in range(n):
            if b == 1:
                # 첫 번째 곡을 맨 끝으로 이동
                playlist.append(playlist.pop(0))
            elif b == 2:
                # 마지막 곡을 맨 앞으로 이동
                playlist.insert(0, playlist.pop())
            elif b == 3:
                # 처음 두 곡의 위치를 서로 바꿈
                playlist[0], playlist[1] = playlist[1], playlist[0]

# 프로그램 실행
simulate_c3mp()
