import datetime
import json

import pytest

from src.clean_scrapping.serializers.player_serializer import PlayerEncoder
from src.clean_scrapping.domain.player import Player


def test_serialize_domain_player():

    player = Player(
        name="Horacio",
        surname="Cifuentes",
        hand="Right"
    )

    expected_json ='{"code":"0a7118315da064bf556ffcc325081f37","name": "Horacio","surname": "Cifuentes","hand": "Right"}'

    json_player = json.dumps(player, cls=PlayerEncoder)

    assert json.loads(json_player) == json.loads(expected_json)


def test_serialize_domain_player_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=PlayerEncoder)
