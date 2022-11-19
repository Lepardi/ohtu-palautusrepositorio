

def filter_by_nationality(player, nationality):
    if player.nationality == nationality:
        return True
    else:
        return False

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        sorted_players = sorted(self.players,
                                key=lambda player: player.goals+player.assists,
                                reverse=True)
        filtered_players = filter(lambda player: 
                                filter_by_nationality(player, nationality),
                                sorted_players)

        return filtered_players

