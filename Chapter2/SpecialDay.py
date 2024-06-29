#(ccc15j1) Special Day

# 2월 18일 이전: Before
# 2월 18일    : Special
# 2월 18일 이후: After
def determine_date_relationship(month, day):
    if month < 2:
        return "Before"
    elif month > 2:
        return "After"
    else:  # 2월
        if day < 18:
            return "Before"
        elif day == 18:
            return "Special"
        else:
            return "After"

# 입력
month = int(input())
day = int(input())
print(determine_date_relationship(month, day))
