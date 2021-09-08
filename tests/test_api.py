import json

def test_get_collection(app_client):
    f = open('tests/test_data/collection.json')
    collection = json.load(f)
    collection_id = collection["id"]
    resp = app_client.post(f"/collections/")

    resp = app_client.get(f"/collections/{collection_id}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["content"]["id"] == collection_id