from flask import Blueprint
from flask import flash
from flask import g
from flask import request
from flask import url_for
import json
from flaskr.db import get_db

bp = Blueprint("search", __name__,url_prefix="/search")

@bp.route("/", methods=("POST",))
def index():
        
    """Search Object."""
    try:
            json_data = request.get_json(force=True)
            if not json_data:
               return {'message': 'No input data provided'}, 400        
                          
            value=json_data['value']                              
            inputquery=json_data['query']            
            field=json_data['field']
            db = get_db()
            cursor=db.cursor()
            data=[]
            if field:
                output={}
                query="SELECT * from Product where {}= '{}' ".format(field,value)
                queryoutput = db.execute(query).fetchall()
                print('Hi')
                productoutput=[]
                for row in queryoutput:
                    a=[]
                    for j in row:
                        a.append(j)
                    productoutput.append(a)    
                output['Product']=productoutput
                print('Hi')
                
                issueresults = db.execute(
                      "SELECT * from Issue where {}= '{}' ".format(field,value)).fetchall()
                issueOutput=[]
                for row in issueresults:
                    a=[]
                    for j in row:
                        a.append(j)
                    issueOutput.append(a)    
                output['Issue']=issueOutput
                metricresults = db.execute(
                              "SELECT * from Metric where {}= '{}' ".format(field,value)).fetchall()
                metricoutput=[]              
                for row in metricresults:
                    a=[]
                    for j in row:
                        a.append(j)
                    metricoutput.append(a)    
                output['Metric']=metricoutput  
    
                return output,200     
                      

  
                  
            if inputquery:
                results = db.execute("""SELECT * FROM 
                (SELECT PRODUCT_ID,Title,Description FROM Product  
                where Product_ID like ? or Title like ? or Description like ?) A 
                 JOIN
                (SELECT IssueID,Title,Category,PRODUCT_ID FROM Issue 
                where IssueID like  ?  or Title like ?  or Category like ?  or Product_ID like  ? OR METRIC_ID LIKE  ? ) B
                ON A.PRODUCT_ID=B.PRODUCT_ID
                 JOIN
                    (SELECT MetricID,Title,Description,PRODUCT_ID FROM Metric where MetricID like ? or Title like  ? or Description like ? 
                or Product_ID like ? ) C
                ON A.PRODUCT_ID=C.PRODUCT_ID """,(inputquery,str(inputquery),str(inputquery),
                inputquery,str(inputquery),str(inputquery),
                inputquery,inputquery,str(inputquery),str(inputquery),inputquery,inputquery)         
                ).fetchall()   
            for i in results:
                a=[]
                for j in i:
                    a.append(j)
                data.append(a)    
            print(data)        
            
            
            #data=[dict(zip ([key[0] for key in cursor.description] ,row)) for row in results]
            return json.dumps(data), 200       
            
    except Exception as identifier:
        print(identifier.args)
        return json.dumps(identifier.args),500

   


