import sys

def calculate_points(deck):
    scores = {'A': 0, 'B': 0}
    high_cards = {'ace': 4, 'king': 3, 'queen': 2, 'jack': 1}
    current_player = 'A'

    i = 0
    while i < len(deck):
        card = deck[i]

        if card in high_cards:
            points = high_cards[card]
            if i + points < len(deck):
                next_cards = deck[i + 1:i + 1 + points]
                if not any(c in high_cards for c in next_cards):
                    scores[current_player] += points
                    print(f"Player {current_player} scores {points} point(s).")

        # 플레이어 전환 및 인덱스 증가
        current_player = 'A' if current_player == 'B' else 'B'
        i += 1

    print(f"Player A: {scores['A']} point(s).")
    print(f"Player B: {scores['B']} point(s).")

def main():
    deck = sys.stdin.read().strip().lower().splitlines()
    calculate_points(deck)

if __name__ == "__main__":
    main()
