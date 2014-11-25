class PDGame:
    def __init__(self, strat1, strat2):
        # Seeds game with the two strategies
        self.strat1 = strat1
        self.strat2 = strat2

        self.score1 = 0
        self.score2 = 0

        # Stores history of games
        # list of 2-tuples:
        # [(strat1's move, strat2's move), (,), (,), ...]
        self.history = []

        self.result = {}
        self.result['C'] = {'C': (2,2), 'D': (0,3)}
        self.result['D'] = {'C': (3,0), 'D': (1,1)}

    def iterate(self):
        # Executes one step of the game

        # Feed history to each strategy
        play1 = self.strat1.getPlay(self.history, 0)
        play2 = self.strat2.getPlay(self.history, 1)

        # Compute result and update history
        self.score1 = self.score1 + self.result[play1][play2][0]
        self.score2 = self.score1 + self.result[play1][play2][1]
        self.history.append((play1, play2))

class Strategy:
    def __init__(self):
        pass

    def getPlay(self, history, id):
        # given a history of moves, returns a move
        # id = 0 or 1, indicates which player
        return 'C'

class allC(Strategy):
    def getPlay(self, history, id):
        return 'C'

class allD(Strategy):
    def getPlay(self, history, id):
        return 'D'

class TFT(Strategy):
    def getPlay(self, history, id):
        if len(history) == 0:
            return 'C'
        else:
            return history[-1][1-id]
    

if __name__ == '__main__':
    # Execute example
    
    s1 = allD()
    s2 = TFT()

    game = PDGame(s1, s2)
    for i in range(10):
        game.iterate()
    print game.history
