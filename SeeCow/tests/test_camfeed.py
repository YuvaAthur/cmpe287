import pytest
from seecow.db import get_db


def test_index(client, auth):
    response = client.get('/')
    # assert b"Log In" in response.data
    # assert b"Register" in response.data

    