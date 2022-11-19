
class Player:
    def __init__(self, name, goals, assists, nationality):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
    
    def __str__(self):
        return (f"{self.name:24}{self.nationality:4}{self.goals:3} + {self.assists:2} = {self.goals +self.assists:3}")
