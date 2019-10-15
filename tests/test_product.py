import pytest

from flaskr.db import get_db


def test_index(client):
    response = client.get("/product/")
    print(response.data)
    assert b"Product3" in response.data
    assert b"Product3 Description" in response.data
    assert b"11" in response.data


def test_create(client,  app):
    
    assert client.get("/product/").status_code == 200
    respose=client.post("/product/", json={"Title": "Product 4", "Description": "Product 4 Description"})
    
    assert respose.status_code==201
    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(Product_Id) FROM Product").fetchone()[0]
        assert count == 3


def test_update(client, app):
    
    assert client.get("/product/").status_code == 200
    response=client.put("/product/", json={"Title": "Product 4", "Description": "Product 4 Description Changed","Product_Id":11})
    assert response.status_code==202

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM product WHERE Product_Id = 11").fetchone()
        assert result["Title"] == "Product 4"
        assert result["Description"] == "Product 4 Description Changed"




def test_delete(client, app):
    
    response = client.delete("/product/", json={"Product_ID":11})
    assert response.status_code == 204

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Product WHERE Product_ID = 11").fetchone()
        assert result is None

