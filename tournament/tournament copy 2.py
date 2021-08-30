from collections import defaultdict


def tally(rows):
    results_board = defaultdict(lambda: defaultdict(int))

    for row in rows:
        team_a, team_b, outcome = row.split(';')
        results_board[team_a]['matches'] += 1
        results_board[team_b]['matches'] += 1
        if outcome == 'win':
            results_board[team_a]['wins'] += 1
            results_board[team_a]['points'] += 3
            results_board[team_b]['losses'] += 1
        if outcome == 'loss':
            results_board[team_a]['losses'] += 1
            results_board[team_b]['wins'] += 1
            results_board[team_b]['points'] += 3
        if outcome == 'draw':
            results_board[team_a]['draws'] += 1
            results_board[team_a]['points'] += 1
            results_board[team_b]['draws'] += 1
            results_board[team_b]['points'] += 1

    header = dict(Team={'matches': 'MP', 'wins': 'W', 'draws': 'D', 'losses': 'L', 'points': 'P'})
    results_board = dict(sorted(results_board.items(), key=lambda x: (-x[1]['points'], x[0])))

    return [f"{team[0]:31}| {team[1]['matches']:^3}| {team[1]['wins']:^3}| {team[1]['draws']:^3}| "
            f"{team[1]['losses']:^3}| {team[1]['points']:>2}"
            for team in (header | results_board).items()]