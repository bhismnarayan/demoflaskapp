from flask import Blueprint
from flask import flash
from flask import g
from flask import request
from flask import url_for
import json
from flaskr.db import get_db

bp = Blueprint("mapobject", __name__,url_prefix="/mapobject")

@bp.route("/", methods=("POST","GET"))
def index():
        
    """Map Object."""
    if request.method == "POST":
        try:
            json_data = request.get_json(force=True)
            if not json_data:
               return {'message': 'No input data provided'}, 400        
                          
            ProductId=json_data['Product_Id']                     
            IssueId=json_data['IssueId']
            MetricId=json_data['MetricId']             
            db = get_db()
            if IssueId and ProductId:
                results = db.execute(
                       "Update Issue set Product_Id = ? where IssueId=? and ?= (select Product_Id from Product where Product_Id=?)"
                       ,(ProductId,IssueId,ProductId,ProductId)) 
                db.commit() 

            if ProductId and MetricId:
                results = db.execute(
                       "Update Metric set Product_Id = ? where MetricId=? and ?= (select Product_Id from Product where Product_Id=?)"
                       ,(ProductId,MetricId,ProductId,ProductId)) 
                db.commit()                       
                          
            if IssueId and MetricId:
                results = db.execute(
                       "Update Issue set Metric_Id = ? where IssueId=? and ?= (select MetricId from Metric where MetricId=?)"
                       ,(MetricId,IssueId,MetricId,MetricId)) 
                db.commit()

            return { "status": 'success', 'data': 'Data update successfully'}, 202       
            
        except Exception as identifier:
            return json.dumps(identifier.args),500

   


