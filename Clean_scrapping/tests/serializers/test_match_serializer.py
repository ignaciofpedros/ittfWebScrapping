import datetime
import json

import pytest

from src.clean_scrapping.serializers.player_serializer import PlayerEncoder
from src.clean_scrapping.serializers.match_serializer import MatchEncoder
from deepdiff import DeepDiff # type: ignore

from src.clean_scrapping.domain.match import Match
from src.clean_scrapping.domain.player import Player


def test_serialize_domain_match():

    playerH = Player(
        name="Horacio",
        surname="Cifuentes",
        hand="Right"
    )

    playerN = Player(
        name="Nicolas",
        surname="Galvano",
        hand="Right"
    )

    match = Match(
            year=2021,
            tournament="Campeonato de Argentina", 
            player1=playerH, 
            player2=playerN, 
            score="3-2", 
            winner=playerH
    )

    json_match = json.dumps(match, cls=MatchEncoder)

    player1_dict = json.loads(json.dumps(playerH, cls=PlayerEncoder))
    player2_dict = json.loads(json.dumps(playerN, cls=PlayerEncoder))

    expected_json = {
            "code": "3c47a489173d44adec197e9fc5d04705",
            "year": 2021,
            "tournament": "Campeonato de Argentina",
            "player1": player1_dict,
            "player2": player2_dict,
            "score": "3-2",
            "winner": player1_dict
        }
    
    json_compare = json.dumps(expected_json)

    assert json.loads(json_match) == json.loads(json_compare)
    assert not DeepDiff(json_match, json_compare, ignore_order=True)
    assert not DeepDiff(json.loads(json_match), json.loads(json_compare), ignore_order=True)


def test_serialize_domain_match_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=MatchEncoder)
