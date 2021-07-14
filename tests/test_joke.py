from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app
from app.core import settings

client = TestClient(app)


class TestJokeAPI(TestCase):

    def test_api_get_joke(self):
        """
        TODO mock out requests
        """

        response = client.get(f"{settings.API_V1_STR}/jokes")
        assert response.status_code == 200
        rjson = response.json()[0]

        assert 'id' in rjson
        assert 'type' in rjson
        assert 'setup' in rjson
        assert 'punchline' in rjson
        assert 'status' in rjson
