import board


def main():
    with open('bingo', 'r') as file:
        contents = file.read().split("\n\n")
        calls = contents[0].split(',')
        cards = [board.Board(5, card.split()) for card in contents[1:]]

    for call in calls:
        for card in cards:
            card.makeMove(call)
            if card.hasWon():
                print(card.board_score(call))
                print()
                
    


if __name__ == '__main__':
    main()