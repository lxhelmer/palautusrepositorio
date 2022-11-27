class PlayerStats:

    def __init__(self,reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self,country):
        ret = filter(lambda x: (x.nat==country),self.players)
        ret = sorted(list(ret), key = lambda x: (x.goals+x.assists),reverse=True)
        
        return ret
