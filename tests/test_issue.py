import pytest

from flaskr.db import get_db


def test_index(client):
    response = client.get("/issue/")
    print(response.data)
    assert b"Issue1" in response.data
    assert b"Low" in response.data
    assert b"1" in response.data


def test_create(client,  app):
    
    assert client.get("/issue/").status_code == 200
    respose=client.post("/issue/", json={"Title": "created", "Category": "High"})
    
    assert respose.status_code==201
    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(IssueId) FROM issue").fetchone()[0]
        assert count == 3


def test_update(client, app):
    
    assert client.get("/issue/").status_code == 200
    response=client.put("/issue/", json={"Title": "Issue updated", "Category": "Low","IssueId":1})
    assert response.status_code==202

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Issue WHERE IssueId = 1").fetchone()
        assert result["title"] == "Issue updated"
        assert result["Category"] == "Low"




def test_delete(client, app):
    
    response = client.delete("/issue/", json={"IssueId":1})
    assert response.status_code == 204

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Issue WHERE IssueId = 1").fetchone()
        assert result is None

