#(dmopc16c1p0) C.C. and Cheese-kun

def determine_satisfaction(W, C):
    if W == 3 and C >= 95:
        return "C.C. is absolutely satisfied with her pizza."
    elif W == 1 and C <= 50:
        return "C.C. is fairly satisfied with her pizza."
    else:
        return "C.C. is very satisfied with her pizza."

def determin_satisfaction_1(W, C):
    if W == 3 and C >= 95:
        return "absolutely"
    elif W == 1 and C <= 50:
        return "fairly"
    else:
        return "very"

# 피자 사이즈와 치즈 퍼센테이지 입력 받기
W = int(input().strip())  # 피자 사이즈
C = int(input().strip())  # 치즈 퍼센테이지

#result = determine_satisfaction(W, C)
#print(result)

# determine_satisfaction_1 함수를 이용하여 만족도 평가 받기
satisfaction_level = determin_satisfaction_1(W, C)
# 결과 문장 출력
print(f"C.C. is {satisfaction_level} satisfied with her pizza.")
