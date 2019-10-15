from flask import Blueprint
from flask import flash
from flask import g
from flask import request
from flask import url_for
import json
from flaskr.db import get_db

bp = Blueprint("metric", __name__,url_prefix="/metric")

@bp.route("/", methods=("GET", "POST","PUT","DELETE"))
def index():
    "Get All Metric"
    if request.method == "GET":
        try:
            db = get_db()
            results = db.execute("SELECT * from Metric").fetchall()
            data=[]
            for row in results:
                data.append([x for x in row])
    
            return json.dumps(data),200
        except Exception as identifier:
            return identifier.args ,500
        
    """Create a new product."""
    if request.method == "POST":
        try:
            data = request.get_json(force=True)
            if not data:
               return {'message': 'No input data provided'}, 400                
            title=data['Title']                     
            description=data['Description']             
            db = get_db()
            posts = db.execute(
             "INSERT INTO Metric (Title, Description) VALUES (?,?)",(title,description)
                )  
            db.commit()               
            return { "status": 'success', 'data': 'Data added successfully'}, 201      
            
        except Exception as identifier:
            return json.dumps(identifier.args),500

    if request.method == "PUT":
        try:
            
            data=request.get_json()
            if not data:
               return {'message': 'No input data provided'}, 400 
            id=data['MetricId']              
            title=data['Title']                     
            description=data['Description']             
            db = get_db()
            posts = db.execute(
             "UPDATE Metric SET title = ?, description = ? WHERE MetricId = ?", (title, description, id)
                )             
            db.commit()               
            return { "status": 'success', 'data': 'Data updated successfully'}, 202     
            
        except Exception as identifier:
            return json.dumps(identifier.args),500

    if request.method=="DELETE":
        try:
            json_data = request.get_json(force=True)
            if not json_data:
               return {'message': 'No input data provided'}, 400        
            
            db = get_db()           
            results = db.execute("DELETE FROM Metric WHERE MetricID = ?", (json_data['MetricID'],) )             
            db.commit()   
            
            return { "status": 'success', 'data': ' Data deleted successfully'}, 204       
            
        except Exception as identifier:
            print(identifier.args  )
            return json.dumps(identifier.args ),500       



