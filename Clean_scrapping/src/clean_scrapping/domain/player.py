from src.clean_scrapping.shared.domain_model import DomainModel
import hashlib


class Player(object):

    def __init__(self, name, surname, hand):

        self.code = hashlib.md5(f"{name}/{surname}".encode()).hexdigest()
        self.name = name
        self.surname = surname
        self.hand = hand

    @classmethod
    def from_dict(cls, adict):
        player = Player(
            name=adict['name'],
            surname=adict['surname'],
            hand=adict['hand']
        )

        return player

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'surname': self.surname,
            'hand': self.hand,
        }

    def __eq__(self, other):
        return self.code == other.code


DomainModel.register(Player)
