from src.clean_scrapping.shared.domain_model import DomainModel
import hashlib

class Match(object):

    def __init__(self, year, tournament, player1, player2, score, winner):

        if player1.code < player2.code:
            self.code = hashlib.md5(f"{year}/{tournament}/{player1.code}/{player2.code}".encode()).hexdigest()
        else:
            self.code = hashlib.md5(f"{year}/{tournament}/{player2.code}/{player1.code}".encode()).hexdigest()

        self.year = year
        self.tournament = tournament
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.winner = winner

    @classmethod
    def from_dict(cls, adict):
        match = Match(
            year=adict['year'],
            tournament=adict['tournament'],
            player1=adict['player1'],
            player2=adict['player2'],
            score=adict['score'],
            winner=adict['winner']
        )

        return match

    def to_dict(self):
        return {
            'code': self.code,
            'year': self.year,
            'tournament': self.tournament,
            'player1': self.player1,
            'player2': self.player2,
            'score': self.score,
            'winner': self.winner
        }

    def __eq__(self, other):
        
        return self.code == other.code


DomainModel.register(Match)
