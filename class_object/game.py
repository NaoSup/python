# programme principal
class Game:
    def __init__(self, data):
        self.data = data
        self.players = []

    def player(self, name):
        if len(self.players) == 2:
            raise "You cannot add any more players"
        self.players.append({'name':name, 'score':0})

    def run(self):
        if len(self.players) != 2:
            raise "You cannot start the game. You need 2 players.({len(self.players)})"
        
        for data in self.data[1:]:
            d = data.split(' ')
            d1 = int(d[0])
            d2 = int(d[1])

            if d1 == d2:
                continue
            if d1 > d2:
                self.players[0]['score'] += 1
            else:
                self.players[1]['score'] += 1

    def __str__(self):
        p1, p2 = self.players[0], self.players[1]

        if p1['score'] > p2['score']:
            return f"The winner is {p1['name']} with {p1['score']} points."
        elif p1['score'] < p2['score']:
            return f"The winner is {p2['name']} with {p2['score']} points."
        else:
            return "Tied. No winner."

#bootstrap
battle = [
    '19', '3 10', '1 2', '2 6', '1 2', '10 1', '8 5', '8 3', '9 7', '3 4',
    '5 9', '3 7', '3 6', '2 6', '6 10', '7 4', '1 10', '4 1', '9 1', '6 2',
]

game = Game(battle)
game.player('Alan')
game.player('Bob')

game.run()

print(game)
print(game.players)