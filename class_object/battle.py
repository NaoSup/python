class Game:
    
    def __init__(self, battle):
        self.battle = battle
    
    def run(self, battle):
        counterPlayer1 = 0
        counterPlayer2 = 0
        list = []
        for x in range(1, len(battle)):
            list = battle[x].split(' ')
            if int(list[0]) > int(list[1]):
                counterPlayer1 +=1
            elif int(list[1]) > int(list[0]):
                counterPlayer2 +=1
        if counterPlayer1 > counterPlayer2:
            winner = "Player 1"
        elif counterPlayer1 < counterPlayer2:
            winner = "Player 2"
        else: 
            winner = "No winner"
        return winner

battle = [
    '19', '3 10', '1 2', '2 6', '1 2', '10 1', '8 5', '8 3', '9 7', '3 4',
    '5 9', '3 7', '3 6', '2 6', '6 10', '7 4', '1 10', '4 1', '9 1', '6 2',
]

game = Game(battle)
print(game.run(battle))
