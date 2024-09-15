import pytest
import hashlib

from src.clean_scrapping.domain.match import Match
from src.clean_scrapping.domain.player import Player
from src.clean_scrapping.shared.domain_model import DomainModel

from src.clean_scrapping.repository import memrepo


@pytest.fixture
def match_dicts():

    code1 = hashlib.md5("Horacio/Cifuentes".encode()).hexdigest()
    code2 = hashlib.md5("Nicolas/Galvano".encode()).hexdigest()
    code3 = hashlib.md5("Martin/Bentacor".encode()).hexdigest()

    code4 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code2).encode()).hexdigest()
    code5 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code3, code2).encode()).hexdigest()
    code6 = hashlib.md5("2021/Campeonato de Argentina/{}/{}".format(code1, code3).encode()).hexdigest()


    return [
        {
            'code': code4,
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': Player.from_dict(
                {
                    'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'score': '3-2',
            'winner': Player.from_dict(
                {
                    'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            )
        },
        {
            'code': code6,
            'year': 2021,
            'tournament': 'Campeonato de Argentina',
            'player1': Player.from_dict(
                {
                    'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': hashlib.md5("Martin/Bentacor".encode()).hexdigest(),
                    'name': 'Martin',
                    'surname': 'Bentacor',
                    'hand': 'Right'
                }
            ),
            'score': '3-1',
            'winner': Player.from_dict(
                {
                    'code': hashlib.md5("Martin/Bentacor".encode()).hexdigest(),
                    'name': 'Martin',
                    'surname': 'Bentacor',
                    'hand': 'Right'
                }
            )
        },
        {
            'code': code5,
            'year': 2022,
            'tournament': 'Campeonato panamericano',
            'player1': Player.from_dict(
                {
                    'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': hashlib.md5("Martin/Bentacor".encode()).hexdigest(),
                    'name': 'Martin',
                    'surname': 'Bentacor',
                    'hand': 'Right'
                }
            ),
            'score': '3-0',
            'winner': Player.from_dict(
                {
                    'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            )
        },
        {
            'code': code4,
            'year': 2022,
            'tournament': 'Campeonato panamericano',
            'player1': Player.from_dict(
                {
                    'code': hashlib.md5("Horacio/Cifuentes".encode()).hexdigest(),
                    'name': 'Horacio',
                    'surname': 'Cifuentes',
                    'hand': 'Right'
                }
            ),
            'player2': Player.from_dict(
                {
                    'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            ),
            'score': '3-2',
            'winner': Player.from_dict(
                {
                    'code': hashlib.md5("Nicolas/Galvano".encode()).hexdigest(),
                    'name': 'Nicolas',
                    'surname': 'Galvano',
                    'hand': 'Right'
                }
            )
        }
    ]


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.code for dm in domain_models_list]
               ) == set([d['code'] for d in data_list])


def test_repository_list_without_parameters(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(),
        match_dicts
    )


def test_repository_list_with_filters_unknown_key(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    with pytest.raises(KeyError):
        repo.list(filters={'name': 'aname'})


def test_repository_list_with_filters_unknown_operator(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    with pytest.raises(ValueError):
        repo.list(filters={'price__in': [20, 30]})


def test_repository_list_with_filters_price(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(filters={'price': 60}),
        [match_dicts[2]]
    )


def test_repository_list_with_filters_price_eq(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(filters={'price__eq': 60}),
        [match_dicts[2]]
    )


def test_repository_list_with_filters_price_lt(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(filters={'price__lt': 60}),
        [match_dicts[0], match_dicts[3]])


def test_repository_list_with_filters_price_gt(match_dicts):
    repo = memrepo.MemRepo(match_dicts)
    _check_results(
        repo.list(filters={'price__gt': 60}),
        [match_dicts[1]]
    )


def test_repository_list_with_filters_size(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(filters={'size': 93}),
        [match_dicts[3]]
    )


def test_repository_list_with_filters_size_eq(match_dicts):
    repo = memrepo.MemRepo(match_dicts)
    _check_results(
        repo.list(filters={'size__eq': 93}),
        [match_dicts[3]]
    )


def test_repository_list_with_filters_size_lt(match_dicts):
    repo = memrepo.MemRepo(match_dicts)
    _check_results(
        repo.list(filters={'size__lt': 60}),
        [match_dicts[2]]
    )


def test_repository_list_with_filters_size_gt(match_dicts):
    repo = memrepo.MemRepo(match_dicts)
    _check_results(
        repo.list(filters={'size__gt': 400}),
        [match_dicts[1]]
    )


def test_repository_list_with_filters_code(match_dicts):
    repo = memrepo.MemRepo(match_dicts)

    _check_results(
        repo.list(filters={'code': '913694c6-435a-4366-ba0d-da5334a611b2'}),
        [match_dicts[2]]
    )
