from doska import Game

print("Морской бой")

field = [['o'] * 6 for _ in range(6)]


# def show_doska():
#     print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
#     for i in range(len(field)):
#         print(str(i) + ' | ' + ' | '.join(field[i]) + ' |')
#
#
# show_doska()


game = Game()
game.start()
