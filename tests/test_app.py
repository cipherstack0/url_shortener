import pytest
from app import app
from functions import encode

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_index_get(client):
    response = client.get('/')
    
    assert response.status_code == 200
    
def test_post_url(client):
    response = client.post('/', data={ "url": "http://example.com"})
    
    assert response.status_code == 200
    assert b"http://localhost:5000/" in response.data

def test_redirect(client):
    short_url = encode("https://example.com")

    short_code = short_url.replace("http://localhost:5000/", "")

    response = client.get("/" + short_code)

    assert response.status_code == 302
    assert response.location == "https://example.com"
    
def test_post_without_url(client):
    response = client.post('/')

    assert response.status_code == 400
    
def test_redirect_nonexistent(client):
    response = client.get('/does-not-exist')

    assert response.status_code == 404
    assert b'Page not found!' in response.data