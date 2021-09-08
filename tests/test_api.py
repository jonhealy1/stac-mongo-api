import json

def test_get_collection(app_client):
    collection_id = "sentinel-2"
    resp = app_client.get(f"/collections/{collection_id}")
    if resp.status_code != 200:
        f = open('tests/test_data/collection.json')
        collection = json.load(f)
        resp = app_client.post(f"/collections/", json=collection)
    resp_json = resp.json()
    assert resp_json["content"]["id"] == collection_id


def test_get_all_collections(app_client):
    resp = app_client.get(f"/collections")
    if resp.status_code != 200:
        f = open('tests/test_data/collection.json')
        collection = json.load(f)
        resp = app_client.post(f"/collections/", json=collection)
    resp_json = resp.json()
    assert len(resp_json) >= 1

def test_get_item_collection(app_client):
    collection_id = "sentinel-2"
    resp = app_client.get(f"/collections/{collection_id}/items")
    if resp.status_code != 200:
        f = open('tests/test_data/extended-item.json')
        item = json.load(f)
        resp = app_client.post(f"/collections/{collection_id}", json=item)
        resp = app_client.get(f"/collections/{collection_id}/items")
    resp_json = resp.json()
    assert len(resp_json) >= 1

