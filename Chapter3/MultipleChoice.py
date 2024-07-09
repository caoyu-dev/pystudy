#https://dmoj.ca/problem/ccc11s2

def count_correct(N):
    # 학생의 응답을 저장할 리스트
    student_responses = []
    # 정답을 저장할 리스트
    correct_answers = []

    # 학생의 응답을 입력받아 리스트에 저장
    for _ in range(N):
        student_responses.append(input())

    # 정답을 입력받아 리스트에 저장
    for _ in range(N):
        correct_answers.append(input())

    # 정답을 맞춘 수 계산
    correct_count = 0

    # 학생의 응답과 정답을 비교
    for i in range(N):
        if student_responses[i] == correct_answers[i]:
            correct_count += 1

    print(correct_count)

# 문제의 수 입력 받기
N = int(input())
count_correct(N)
