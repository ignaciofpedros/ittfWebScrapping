import hashlib
from src.clean_scrapping.domain.player import Player
from src.clean_scrapping.domain.match import Match


def test_match_model_init():
    code1 = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    code2 = hashlib.md5("Nicolas/Galvano".encode()).hexdigest()

    code3 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code2).encode()).hexdigest()

    player1 = Player(name='Horacio', surname='Cifuentes', hand='Right')
    player2 = Player(name='Nicolas', surname='Galvano', hand='Right')

    match = Match(year=2021,tournament='Campeonato de Argentina', player1=player1, player2=player2, score='3-2', winner=player1)

    assert match.code == code3
    assert match.year == 2021
    assert match.tournament == 'Campeonato de Argentina'
    assert match.player1 == player1
    assert match.player2 == player2
    assert match.score == '3-2'
    assert match.winner == player1


def test_match_model_from_dict():
    code1 = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    code2 = hashlib.md5("Nicolas/Galvano".encode()).hexdigest()

    code3 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code2).encode()).hexdigest()

    match = Match.from_dict(
        {
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': code2,
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'score': '3-2',
            'winner': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            )
        }
    )
    assert match.code == code3  
    assert match.year == 2021
    assert match.tournament == 'Campeonato de Argentina'
    assert match.player1.code == code1
    assert match.player1.name == 'Horacio'
    assert match.player1.surname == 'Cifuentes'
    assert match.player1.hand == 'Right'
    assert match.player2.code == code2
    assert match.player2.name == 'Nicolas'
    assert match.player2.surname == 'Galvano'
    assert match.player2.hand == 'Right'
    assert match.score == '3-2'
    assert match.winner.code == code1
    assert match.winner.name == 'Horacio'
    assert match.winner.surname == 'Cifuentes'
    assert match.winner.hand == 'Right'


def test_match_model_to_dict():
    code1 = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    code2 = hashlib.md5("Nicolas/Galvano".encode()).hexdigest()

    player1 = Player(name='Horacio', surname='Cifuentes', hand='Right')
    player_dict1 = {
        'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
        'name': 'Nicolas',
        'surname': 'Galvano',
        'hand': 'Right'
    }
    player2 = Player.from_dict(player_dict1)

    match_dict = (
        {
            'code': hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code2).encode()).hexdigest(),
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': player1,
            'player2': player2,
            'score': '3-2',
            'winner': player1
        }
    )

    match = Match.from_dict(match_dict)

    assert match.to_dict() == match_dict


def test_match_model_comparison():
    player1 = Player(name='Horacio', surname='Cifuentes', hand='Right')
    player2 = Player(name='Nicolas', surname='Galvano', hand='Right')
    code1 = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    code2 = hashlib.md5("Nicolas/Galvano".encode()).hexdigest()

    code3 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code2).encode()).hexdigest()

    match_dict1 = (
        {
            'code': code3,
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': code2,
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'score': '3-2',
            'winner': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            )
        }
    )

    match_dict2 = (
        {
            'code': code3,
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': Player.from_dict(
                {
                    'code': code2,
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'score': '3-2',
            'winner': Player.from_dict(
                {
                    'code': code1,
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            )
        }
    )

    match1 = Match.from_dict(match_dict1)
    match2 = Match.from_dict(match_dict1)
    match3 = Match.from_dict(match_dict2)
    match4 = Match(year=2021,tournament='Campeonato de Argentina', player1=player2, player2=player1, score='3-2', winner=player1)

    assert match1 == match2
    assert match1 == match3
    assert match1 == match4
