# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
player1 = None
player2 = None
chosen_numbers = []

class Player:
    def won(self):
        self.choosenFields.sort()
        return self.choosenFields in [[1,2,3], [4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def choose_number(self, number):
        self.choosenFields.append(int(number))

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choosenFields = []


def get_names():
    print(f'Hello :) What is the name of Player1?')
    name = input()
    global player1
    player1 = Player(name)
    print(f'Hello :) What is the name of Player2?')
    name = input()
    global player2
    player2 = Player(name)

def game_over():
    chosen_numbers.sort()
    if chosen_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Nobody won")
        return True

def choose(player_name):
    print("Which number do you want to choose, %s?" % player_name)
    chosen_number = input()
    while chosen_number in chosen_numbers or not chosen_number.isdigit():
        print("Please choose a possible number")
        chosen_number = input()
    chosen_numbers.append(int(chosen_number))
    return chosen_number

def game():
    get_names()
    game_board = f'| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |'
    global player1
    global player2
    while True:
        for player in [player1, player2]:
            if game_over():
                return 1
            print(game_board)
            chosen_number = choose(player.name)
            player.choose_number(chosen_number)
            if player.won():
                print("You won, %s!" % player.name)
                return 1
            game_board = game_board.replace(str(chosen_number), "X") if player is player1 else game_board.replace(
                str(chosen_number), "O")


if __name__ == '__main__':
    game()

