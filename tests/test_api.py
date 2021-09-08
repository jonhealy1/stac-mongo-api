def test_get_collection(app_client):
    collection = "sentinel-2"
    resp = app_client.get(f"/collections/{collection}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["content"]["id"] == collection