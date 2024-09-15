from src.clean_scrapping.domain.player import Player
import hashlib

def test_player_model_init():
    code = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    player = Player(name='Horacio', surname='Cifuentes', hand='Right')

    assert player.code == code
    assert player.name == 'Horacio'
    assert player.surname == 'Cifuentes'
    assert player.hand == 'Right'


def test_player_model_from_dict():
    code = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()

    player = Player.from_dict(
        {
            'name': 'Horacio',
            'surname': 'Cifuentes',
            'hand': 'Right'
        }
    )
    assert player.code == code
    assert player.name == 'Horacio'
    assert player.surname == 'Cifuentes'
    assert player.hand == 'Right'


def test_player_model_to_dict():
    player_dict = {
        'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
        'name': 'Horacio',
        'surname': 'Cifuentes',
        'hand': 'Right'
    }

    player = Player.from_dict(player_dict)

    assert player.to_dict() == player_dict


def test_player_model_comparison():
    player_dict = {
        'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
        'name': 'Horacio',
        'surname': 'Cifuentes',
        'hand': 'Right'
    }

    player1 = Player.from_dict(player_dict)
    player2 = Player.from_dict(player_dict)

    assert player1 == player2
