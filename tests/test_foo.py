import json

import pytest
from django.urls import reverse


@pytest.fixture(scope="module")
def foo():
    # set up code
    yield "bar"
    # tear down code


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client):
    # Given
    # client

    # When
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)

    # Then
    assert response.status_code == 200
    assert content["ping"] == "pong!"
