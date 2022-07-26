"""
competitions = [[team1, team2], [team2, team3], [team1, team3]]
results = [1, 0, 1] 

competition[n][0] = homeTeam
competition[n][1] = awayTeam

if result 1 -> HomeTeam wins
else awayTeam wins

"""

# O(n) --Time | O(1) --Space

# Create a variable to hold current best scorer
# Create a dictionary to hold winning teams and scores
# Traverse the arrays that are of same length
# Update the scores if

import unittest


def tournamentWinner(competitions, results):
    winner = ""
    scores = {winner: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == 1 else awayTeam
        updateScores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[winner]:
            winner = winningTeam

    return winner


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)
