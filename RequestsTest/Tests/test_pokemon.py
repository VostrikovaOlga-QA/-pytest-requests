import requests
import pytest

URL='https://api.pokemonbattle.me:9104'

HEADER = {"Content-type": "application/json", 
         "trainer_token": "5305af55c6f00f16b23dc8e02d4ddc8b"
         }

def test_get_trainers():
    """
    TTI-1. Get trainers kod 200

    """
    response=requests.get(url=f'{URL}/trainers',timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_id():
    """
    TTI-2. Get trainers by id

    """
    response=requests.get(url=f'{URL}/trainers',params= {"trainer_id": 4698}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'