#https://usaco.org/index.php?page=viewproblem2&cpid=855

def mix_milk(capacities, amounts, operations = 100):
    for i in range(operations):
        current_bucket = i % 3
        next_bucket = (i + 1) % 3

        pour_amount = min(amounts[current_bucket], capacities[next_bucket] - amounts[next_bucket])
        amounts[current_bucket] -= pour_amount
        amounts[next_bucket] += pour_amount

    return amounts

def main():
    # sample input
    capacities = [10, 11, 12]
    amounts = [3, 4, 5]

    # result
    result = mix_milk(capacities, amounts)

    # print
    for amount in result:
        print(amount)

if __name__ == "__main__":
    main()
