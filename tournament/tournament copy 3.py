from collections import defaultdict
from operator import itemgetter
from typing import Counter, DefaultDict, List, Sequence, Tuple, Union

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}


Cell = Union[str, int]
Row = Tuple[str, Cell, Cell, Cell, Cell, Cell]

def tally1(results: Sequence[str]) -> List[str]:
    """
    Tally a football tournament.
    """
    teams: DefaultDict[str, Counter[str]] = DefaultDict(Counter)
    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1

    table: List[Row] = []
    for team, record in sorted(teams.items()):
        wins, draws, losses = record["win"], record["draw"], record["loss"]
        matches, points = wins + draws + losses, 3 * wins + draws
        table.append((team, matches, wins, draws, losses, points))
    table.sort(key=itemgetter(-1), reverse=True)

    table.insert(0, ("Team", "MP", "W", "D", "L", "P"))
    return [ROW_FORMAT.format(*row) for row in table]

def tally(rows):
    # nested dictionary
    games = defaultdict(lambda: defaultdict(int))

    for row in rows:
        a, b, outcome = row.split(';')
        games[a]['played'] += 1
        games[b]['played'] += 1
        if outcome == 'win':
            games[a]['points'] += 3
            games[a]['wins'] += 1
            games[b]['losses'] += 1
        if outcome == 'loss':
            games[a]['losses'] += 1
            games[b]['points'] += 3
            games[b]['wins'] += 1
        if outcome == 'draw':
            games[a]['draws'] += 1
            games[a]['points'] += 1
            games[b]['draws'] += 1
            games[b]['points'] += 1

    header = dict(Team={'played': 'MP', 'wins': 'W', 'draws': 'D', 'losses': 'L', 'points': 'P'})
    # sorted by name, points
    games = dict(sorted(games.items(), key=lambda x: (-x[1]['points'], x[0])))

    return [ROW_FORMAT.format(r[0], r[1]['played'], r[1]['wins'], 
        r[1]['draws'], r[1]['losses'], r[1]['points']) 
        for r in {**header, **games}.items()]
