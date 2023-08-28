class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, input_player):
        self.players.append(input_player)

    def has_player(self, input_player):
        return input_player in self.players
    
    def play_game(self, input_result):
        if input_result == True:
            self.points += 3