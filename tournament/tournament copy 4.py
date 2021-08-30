from collections import defaultdict

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

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




from pdb import set_trace as bp

class Team:
    def __init__(self, name='', played=0, wins=0, losses=0, draws=0, points=0):
        self.name = name
        self.played = played
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points

    def __iter__(self):
        for each in self.__dict__.values():
            yield each

    def __repr__(self):
        return "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format(self.name, self.played, self.wins, self.draws, self.losses, self.points)

def tally1(rows):
    # nested dictionary
    games = defaultdict(Team)

    for row in rows:
        a, b, outcome = row.split(';')
        team_a, team_b = games[a], games[b]
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
        games[a], games[b] = team_a, team_b
 
    # sorted by points descending, name
    games = sorted(games.values(), key=lambda x: (-x.points, x.name))
    print(games)
    bp()
    table = [ROW_FORMAT.format(*g) for g in games]
    table.insert(0, ROW_FORMAT.format("Team", "MP", "W", "D", "L", "P"))
    return table
