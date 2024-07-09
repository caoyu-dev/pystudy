#https://dmoj.ca/problem/coci12c5p1

def determine_scale(notes):
    a_minor_main_tones = {'A', 'D', 'E'}
    c_major_main_tones = {'C', 'F', 'G'}

    # 음표를 마디로 나누기 위한 리스트 초기화
    measures = []
    current_measure = []

    # 입력 문자열을 순회
    for note in notes:
        if note == '|':
            # '|' 를 만나면 현재 마디를 마디 리스트에 추가
            if current_measure:
                measures.append(current_measure)
                current_measure = []
        else:
            # 음표를 현재 마디에 추가
            current_measure.append(note)

    # 마지막 마디를 리스트에 추가
    if current_measure:
        measures.append(current_measure)

    # 각 마디의 첫 음표 분석을 위해 변수 초기화
    a_minor_count = 0
    c_major_count = 0
    accented_tones = []

    # 각 마디의 첫 음표를 순회
    for measure in measures:
        if measure:
            first_note = measure[0]
            accented_tones.append(first_note)
            if first_note in a_minor_main_tones:
                a_minor_count += 1
            if first_note in c_major_main_tones:
                c_major_count += 1

    # 결과 결정
    if a_minor_count == c_major_count:
        # 주요 음표 갯수가 같으면 마지막 음표로 결정
        last_note = notes[-1]
        if last_note == 'A':
            return 'A-mol'
        elif last_note == 'C':
            return 'C-dur'
    elif a_minor_count > c_major_count:
        return 'A-mol'
    else:
        return 'C-dur'

# 입력 예제
print(determine_scale(input()))

