#(ccc06j1) Canadian Calorie Counting

def calculate_calories():
    # 버거 선택에 따른 칼로리 정의
    # 1. Cheeseburger: 461
    # 2. Fish Burger: 431
    # 3. Veggie Burger: 420
    # 4. no burger: 0
    burger_choices = {
        1: 461, 2: 431, 3: 420, 4: 0
    }

    # 사이드 선택에 따른 칼로리 정의
    # 1. Fries: 100
    # 2. Baked Potato: 57
    # 3. Chef Salad: 70
    # 4. no side order: 0
    side_choices = {
        1: 100, 2: 57, 3: 70, 4: 0
    }

    # 음료 선택에 따른 칼로리 정의
    # 1. Soft Drink: 130
    # 2. Orange Juice: 160
    # 3. Milk: 118
    # 4. no drink: 0
    drink_choices = {
        1: 130, 2: 160, 3: 118, 4: 0
    }

    # 디저트 선택에 따른 칼로리 정의
    # 1. Apple Pie: 167
    # 2. Sundae: 266
    # 3. Fruit Cup: 75
    # 4. no dessert: 0
    dessert_choices = {
        1: 167, 2: 266, 3: 75, 4: 0
    }

    # 각 항목에 대한 숫자 입력
    burger_choice = int(input())
    side_choice = int(input())
    drink_choice = int(input())
    dessert_choice = int(input())

    # 총 칼로리 계산
    total_calories = (
            burger_choices[burger_choice] +
            side_choices[side_choice] +
            drink_choices[drink_choice] +
            dessert_choices[dessert_choice]
    )

    # 계산한 총 칼로리 표기
    print(f"Your total Calorie count is {total_calories}.")

# 프로그램 실행 함수
calculate_calories()
