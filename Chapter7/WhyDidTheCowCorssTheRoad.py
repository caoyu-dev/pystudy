def count_inversions(arr):
    if len(arr) < 2:
        return 0, arr
    mid = len(arr) // 2
    left_inv, left_arr = count_inversions(arr[:mid])
    right_inv, right_arr = count_inversions(arr[mid:])
    cross_inv, merged_arr = merge_and_count(left_arr, right_arr)
    return left_inv + right_inv + cross_inv, merged_arr

def merge_and_count(left, right):
    result = []
    i = j = 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return inversions, result

def calculate_inversions(q, n):
    return count_inversions(q[1:n+1])[0]

def min_crossing_pairs(n, q1, q2):
    inv1 = [0] * (n + 1)
    inv2 = [0] * (n + 1)

    for i in range(1, n + 1):
        inv1[q1[i]] = i
        inv2[q2[i]] = i

    copy1 = [inv2[q1[i]] for i in range(1, n + 1)]
    copy2 = [inv1[q2[i]] for i in range(1, n + 1)]

    response = float('inf')

    for copy in [copy1, copy2]:
        current_inversions = calculate_inversions([0] + copy, n)
        min_inversions = current_inversions

        for i in range(n, 0, -1):
            current_inversions += 2 * copy[i - 1] - n - 1
            min_inversions = min(min_inversions, current_inversions)

        response = min(response, min_inversions)

    return response

if __name__ == "__main__":
    with open("mincross.in", "r") as infile:
        n = int(infile.readline().strip())
        q1 = [0] + [int(infile.readline().strip()) for _ in range(n)]
        q2 = [0] + [int(infile.readline().strip()) for _ in range(n)]

    result = min_crossing_pairs(n, q1, q2)

    with open("mincross.out", "w") as outfile:
        outfile.write(f"{result}\n")
