import pytest

from flaskr.db import get_db




#Test search object scenarios  based on Product 1
def test_create(client,  app):
    
    
    respose=client.post("/search/", json={"query": "33", "field": "null","value":"null"})
    
    assert respose.status_code==200
    assert respose.data == b'[[33, "Product33", "Product33 Description", 2, "Issue333", "Low", 33, 2, "Metric3333", "Metric 3333 Description", 33]]'
   

