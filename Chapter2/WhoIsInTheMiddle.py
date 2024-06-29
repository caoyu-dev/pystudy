#(ccc07j1) Who is in the Middle

def find_mama_bear_bowl(w1, w2, w3):
    # 무게 리스트
    weights = [w1, w2, w3]

    # 무게 순서 정리
    sorted_weights = sorted(weights)

    # 정리된 값들 중 중간 노출
    return sorted_weights[1]

# 무게 입력
w1 = int(input())
w2 = int(input())
w3 = int(input())

# 엄마 보울을 찾기 위한 함수 실행
mama_bear_bowl = find_mama_bear_bowl(w1, w2, w3)

# 결과 표기
print(mama_bear_bowl)
