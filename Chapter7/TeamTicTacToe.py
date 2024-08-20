def check_individual_wins(board):
    winners = set()

    for i in range(3):
        # row
        if board[i][0] == board[i][1] == board[i][2]:
            winners.add(board[i][0])

        # column
        if board[0][i] == board[1][i] == board[2][i]:
            winners.add(board[0][i])

    # diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        winners.add(board[0][0])

    if board[0][2] == board[1][1] == board[2][0]:
        winners.add(board[0][2])

    return len(winners)

def cheack_team_wins(board):
    teams = set()

    def check_line(c1, c2, c3):
        if len(set([c1, c2, c3])) == 2:
            teams.add(tuple(sorted([c1, c2])))

    for i in range(3):
        check_line(board[i][0], board[i][1], board[i][2]) # row
        check_line(board[0][i], board[1][i], board[2][i]) # column

    # diagonal
    check_line(board[0][0], board[1][1], board[2][2])
    check_line(board[0][2], board[1][1], board[2][0])

    return len(teams)

def main():
    with open("tttt.in", "r") as infile:
        board = [infile.readline().strip() for _ in range(3)]

    individual_wins = check_individual_wins(board)
    team_wins = cheack_team_wins(board)

    with open("tttt.out", "w") as outfile:
        outfile.write(f"{individual_wins}\n")
        outfile.write(f"{team_wins}\n")

if __name__ == "__main__":
    main()
