import pytest

from flaskr.db import get_db




def test_update(client, app):
    
    
    response=client.post("/mapobject/", json={"Product_Id": 11, "IssueId": 1,"MetricId":"null"})
    print(response.data)
    assert response.status_code==202

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Issue WHERE IssueId = 1").fetchone()
        assert result["Product_Id"] == 11
       
def test_updatefailedcondition(client, app):
    
    
    response=client.post("/mapobject/", json={"Product_Id": 12, "IssueId": 1,"MetricId":None})
    assert response.status_code==202

    with app.app_context():
        db = get_db()
        result = db.execute("SELECT * FROM Issue WHERE IssueID = 1").fetchone()
        assert result["Product_Id"] == None




