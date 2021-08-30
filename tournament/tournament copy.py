from collections import defaultdict
import csv
from enum import Enum

HEADER = "Team                           | MP |  W |  D |  L |  P"


class MatchResult(Enum):
    WIN = (1, 3)
    DRAW = (0, 1)
    LOSS = (-1, 0)

    def __new__(cls, value, points):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.points = points
        return obj

    def __neg__(self):
        return self.__class__(-self.value)


class TeamResults:
    def __init__(self):
        self.played = 0
        self.record = defaultdict(int)
        self.points = 0

    def register_match(self, result: MatchResult):
        self.played += 1
        self.record[result] += 1
        self.points += result.points

    @property
    def wins(self):
        return self.record[MatchResult.WIN]

    @property
    def draws(self):
        return self.record[MatchResult.DRAW]

    @property
    def losses(self):
        return self.record[MatchResult.LOSS]


class Tournament:
    def __init__(self):
        self.teams = defaultdict(TeamResults)

    def register_match(self, home_team, away_team, result):
        self.teams[home_team].register_match(result)
        self.teams[away_team].register_match(-result)

    def table(self):
        result = [HEADER]
        for team, results in sorted(self.teams.items(), key=lambda v: (-v[1].points, v[0])):
            result.append("%-30s | %2s | %2s | %2s | %2s | %2s" % (
                team,
                results.played,
                results.wins,
                results.draws,
                results.losses,
                results.points,
            ))
        return result

class Team:
    def __init__(self, name='', played=0, win=0, loss=0, draw=0, point=0):
        self.name = name
        self.played = played
        self.win = win
        self.loss = loss
        self.draw = draw
        self.point = point
    def __repr__(self):
        return "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format(self.name, self.played, self.win, self.loss, self.draw, self.point)

scoreBoard = {}
def tally(rows):
    tournament = Tournament()
    for row in csv.reader(rows, delimiter=";"):
        tournament.register_match(row[0], row[1], MatchResult[row[2].upper()])
    return tournament.table()

def tally0(rows):
    board = defaultdict()
    for row in csv.reader(rows, delimiter=";"):




        tournament.register_match(row[0], row[1], MatchResult[row[2].upper()])
    return tournament.table()
