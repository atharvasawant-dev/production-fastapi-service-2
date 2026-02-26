from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_create_list_get_delete():
    r = client.post('/v1/work-items', json={'title': 'Ship feature', 'description': 'Implement X'})
    assert r.status_code == 201
    item = r.json()
    assert item['id'] == 1

    r = client.get('/v1/work-items')
    assert r.status_code == 200
    assert len(r.json()) == 1

    r = client.get('/v1/work-items/1')
    assert r.status_code == 200

    r = client.delete('/v1/work-items/1')
    assert r.status_code == 204
