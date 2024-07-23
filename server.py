from flask import Flask,request , jsonify
import product_dao
import orders_dao
from sql_connection import get_sql_connection
import json



app = Flask(__name__)

connection = get_sql_connection() 

@app.route('/getproducts' , methods = ['GET'])
def getproducts():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Orgin' , '*')
    return response


@app.route('/insertorder' , methods =['GET' ,'POST'])
def insert_order():
    request_payload = json.loads(request.form.get('data', '{}'))    
    order_id = orders_dao.insert_order(connection,request_payload)
    response = jsonify({
        'order_id' : order_id
    })
    response.headers.add('Access-Control-Allow-Orgin' , '*')
    return response

@app.route('/getallorders' , methods = ['GET' , 'POST'])
def get_all_orders_details(): 
    response = orders_dao.get_all_orders_details(connection)
    response = jsonify(response)
    response.headers.add('Access=Control-Allow-Orgin' , '*')
    return response 

if __name__ == "__main__":
    print("starting python Flask Server For Grocery Store Management System")
    app.run(debug=True)