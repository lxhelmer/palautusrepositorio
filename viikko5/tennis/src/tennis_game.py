class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0
        self.scores = {0:"Love",
                       1:"Fifteen",
                       2:"Thirty",
                       3:"Forty"
                    }


    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):

        if self.score1 >= 4 or self.score2 >= 4:
            score = self.overtime()

        elif self.score1 == self.score2:
            score = self.tie()
            
        else: 
            score = self.low_scores()
        return score

    def tie(self):
          
            return self.scores[self.score1] + "-All"


    def overtime(self):
        distance = (self.score1-self.score2)
        if distance == 0:
            return ("Deuce")
        elif distance == 1:
            return ("Advantage player1")
        elif distance == -1:
            return ("Advantage player2")
        elif distance >= 2:
            return ("Win for player1")
        else:
            return ("Win for player2")
    
    def low_scores(self):
           return self.scores[self.score1] + "-" + self.scores[self.score2]

