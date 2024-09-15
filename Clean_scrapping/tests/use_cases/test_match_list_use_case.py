import pytest
from unittest import mock

from src.clean_scrapping.domain.match import Match
from src.clean_scrapping.domain.player import Player
from src.clean_scrapping.shared import response_object as res
from src.clean_scrapping.use_cases import request_objects as req
from src.clean_scrapping.use_cases import match_use_cases as uc


@pytest.fixture
def domain_matches():

    player1 = Player(name='Horacio', surname='Cifuentes', hand='Right')
    player2 = Player(name='Nicolas', surname='Galvano', hand='Right')
    player3 = Player(name='Martin', surname='Bentacor', hand='Right')

    match_1 = Match(
        year=2021,
        tournament='Campeonato de Argentina', 
        player1=player1, 
        player2=player2, 
        score='3-2', 
        winner=player1
    )

    match_2 = Match(
        year=2021,
        tournament='Campeonato de Argentina', 
        player1=player1, 
        player2=player3, 
        score='3-1', 
        winner=player3
    )

    match_3 = Match(
        year=2022,
        tournament='Campeonato panamericano', 
        player1=player2, 
        player2=player3, 
        score='3-0', 
        winner=player2
    )

    match_4 = Match(
        year=2022,
        tournament='Campeonato panamericano', 
        player1=player1, 
        player2=player2, 
        score='3-2', 
        winner=player2
    )

    return [match_1, match_2, match_3, match_4]


def test_match_list_without_parameters(domain_matches):
    repo = mock.Mock()
    repo.list.return_value = domain_matches

    match_list_use_case = uc.MatchListUseCase(repo)
    request_object = req.MatchListRequestObject.from_dict({})

    response_object = match_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_matches


def test_match_list_with_filters(domain_matches):
    repo = mock.Mock()
    repo.list.return_value = domain_matches

    match_list_use_case = uc.MatchListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = req.MatchListRequestObject.from_dict({'filters': qry_filters})

    response_object = match_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_matches


def test_match_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    match_list_use_case = uc.MatchListUseCase(repo)
    request_object = req.MatchListRequestObject.from_dict({})

    response_object = match_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_match_list_handles_bad_request():
    repo = mock.Mock()

    match_list_use_case = uc.MatchListUseCase(repo)
    request_object = req.MatchListRequestObject.from_dict({'filters': 5})

    response_object = match_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }
