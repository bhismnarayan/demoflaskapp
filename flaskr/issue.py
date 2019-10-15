from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import json

from flaskr.db import get_db

bp = Blueprint("issue", __name__,url_prefix="/issue")

@bp.route("/", methods=("GET", "POST","PUT","DELETE"))
def index():
    "Get All Product"
    if request.method == "GET":
        try:
            db = get_db()
            results = db.execute("SELECT * from Issue").fetchall()
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
            Category=data['Category']             
            db = get_db()
            posts = db.execute(
             "INSERT INTO Issue (Title, Category) VALUES (?,?)",(title,Category)
                )  
            print(posts.rowcount)               
            db.commit()               
            return { "status": 'success', 'data': 'Data added successfully'}, 201     
            
        except Exception as identifier:
            return json.dumps(identifier.args),500

    if request.method == "PUT":
        try:
            
            data=request.get_json()
            if not data:
               return {'message': 'No input data provided'}, 400 
            IssueId=data['IssueId']              
            title=data['Title']                     
            Category=data['Category']             
            db = get_db()
            posts = db.execute(
             "UPDATE Issue SET title = ?, Category = ? WHERE IssueId = ?", (title, Category, IssueId)
                )             
            db.commit()               
            return { "status": 'success', 'data': 'Data updated successfully'}, 202      
            
        except Exception as identifier:

            return json.dumps(identifier.args)

    if request.method=="DELETE":
        try:
            json_data = request.get_json(force=True)
            if not json_data:
               return {'message': 'No input data provided'}, 400        
            
            db = get_db()           
            results = db.execute("DELETE FROM Issue WHERE IssueId = ?", (json_data['IssueId'],) )             
            db.commit()   
            
            return { "status": 'success', 'data': ' Data deleted successfully'}, 204       
            
        except Exception as identifier:
            print(identifier.args  )
            return json.dumps(identifier.args ),500       



