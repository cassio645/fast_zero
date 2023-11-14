from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_200_e_hello_world():
    client = TestClient(app) # Arrange

    response = client.get('/') # Act

    # Asserts
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World!'}
