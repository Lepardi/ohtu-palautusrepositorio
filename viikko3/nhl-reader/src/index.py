from player_reader import PlayerReader
from playerstats import PlayerStats

def main():

    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

    # url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    # response = requests.get(url).json()

    # print(response)

    # players = []
    # for player_dict in response:
    #     player = Player(
    #         player_dict['name'],
    #         player_dict['goals'],
    #         player_dict['assists'],
    #         player_dict['nationality']
    #     )
    #     players.append(player)

    # sorted_players = sorted(players,
    #                         key=lambda player: player.goals+player.assists,
    #                         reverse=True)
    # filtered_players = filter(filter_finns, sorted_players)

    # for player in filtered_players:
    #     print(player)
        



if __name__ == "__main__":
    main()

