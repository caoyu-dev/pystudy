#https://dmoj.ca/problem/coci18c3p1

def count_honi_blocks(word):
    # HONI 블록 변수
    target = 'HONI'
    target_idx = 0  # HONI 문자의 인덱스
    honi_count = 0  # HONI 블록 수

    # 입력된 단어의 문자를 순회
    for char in word:
        # 현재 문자가 HONI 의 target_idx 번째 문자와 일치하는지를 확인
        if char == target[target_idx]:
            target_idx += 1
            # HONI 를 모두 찾으면 카운트 증가 후, 인덱스를 다시 0 으로 초기화
            if target_idx == 4:
                honi_count += 1
                target_idx = 0

    print(honi_count)

# 입력을 받고 함수를 호출하여 결과 출력
count_honi_blocks(input())
