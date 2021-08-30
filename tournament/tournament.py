from collections import defaultdict
from typing import Counter, DefaultDict, List, Sequence, Tuple, Union

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

class Team:
    def __init__(self, name='', played=0, wins=0, draws=0, losses=0, points=0):
        self.name = name
        self.played = played
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.points = points

    def __iter__(self):
        for each in self.__dict__.values():
            yield each

    def __repr__(self):
        return ROW_FORMAT.format(*self)

def tally(rows: Sequence[str]) -> List[str]:
    games: DefaultDict[str, Team] = defaultdict(Team)

    for row in rows:
        a, b, outcome = row.split(';')
        team_a, team_b = games[a], games[b] #defaultdict factory
        team_a.name, team_b.name = a, b
        team_a.played += 1
        team_b.played += 1
        if outcome == 'win':
            team_a.points += 3
            team_a.wins += 1
            team_b.losses += 1
        if outcome == 'loss':
            team_a.losses += 1
            team_b.points += 3
            team_b.wins += 1
        if outcome == 'draw':
            team_a.draws += 1
            team_a.points += 1
            team_b.draws += 1
            team_b.points += 1
        games[a], games[b] = team_a, team_b # updating
 
    # sorted by points descending, name
    games = sorted(games.values(), key=lambda x: (-x.points, x.name))

    table: List[str] = [ROW_FORMAT.format(*g) for g in games]
    table.insert(0, ROW_FORMAT.format("Team", "MP", "W", "D", "L", "P"))
    return table
