import pytest

from flaskr.db import get_db


def test_index(client):
    response = client.get("/metric/")
    print(response.data)
    assert b"Metric" in response.data
    assert b"Metric 1 Description" in response.data
    assert b"1" in response.data


def test_create(client,  app):
    
    assert client.get("/metric/").status_code == 200
    respose=client.post("/metric/", json={"Title": "Metric2", "Description": "Metric2 Description"})
    
    assert respose.status_code==201
    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(MetricID) FROM Metric").fetchone()[0]
        assert count == 3


def test_update(client, app):
    
    assert client.get("/metric/").status_code == 200
    response=client.put("/metric/", json={"Title": "Metric2", "Description": "Metric 2 Description Changed","MetricId":1})
    assert response.status_code==202

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Metric WHERE MetricID = 1").fetchone()
        assert result["Title"] == "Metric2"
        assert result["Description"] == "Metric 2 Description Changed"




def test_delete(client, app):
    
    response = client.delete("/metric/", json={"MetricID":1})
    assert response.status_code == 204

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Metric WHERE MetricID = 1").fetchone()
        assert result is None

