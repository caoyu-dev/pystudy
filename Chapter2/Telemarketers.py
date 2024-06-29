# 입력된 네 자리의 전화번호
digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())

# 텔레마케터 전화번호를 확인하는 연산
# 텔레마케터 전화번호 : 첫 번쨰 숫자는 8 또는 9, 네 번쨰 숫자는 8 또는 9, 두 번쨰와 세 번째 숫자는 동일한 경우
if (digit1 == 8 or digit1 == 9) and (digit4 == 8 or digit4 == 9) and (digit2 == digit3):
    print("ignore")
else:
    print("answer")
