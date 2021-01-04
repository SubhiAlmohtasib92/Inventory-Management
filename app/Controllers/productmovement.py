  
from flask import Blueprint, render_template,flash,url_for,request,redirect
import os
from app.Util.dbUtil import GetMovements
from app.Util.dbUtil import GetDB
from app.Util.dbUtil import GetData
from app.Util.dbUtil import GetProductLocations
from app.Util.dbUtil import GetProductQuantity
from app.Util.dbUtil import GetFreeProductQuantity
from app.Util.dbUtil import GetCurrentQty
import uuid
from flask import jsonify

template_dir = os.path.abspath('app/views/movements')

movements_blueprint = Blueprint('movements', __name__, template_folder=template_dir,url_prefix='/movements/')

@movements_blueprint.route('/home')
def index():
    movements=GetMovements()
    products=GetData('product','productname')
    locations=GetData('location','adddate')
    return render_template('movements/index.html',movementsList=movements,locationsList=locations,productList=products)

@movements_blueprint.route('/Get_Product_Locations')
def background_process_test():
    productID = request.args.get('productID')
    locations= GetProductLocations(productID)
    return jsonify(locations)



@movements_blueprint.route('/Get_Product_Quantity')
def Get_Product_Quantity():
    productID = request.args.get('productID')
    Qty= GetProductQuantity(productID)
    return jsonify(Qty)

@movements_blueprint.route('/handle_data', methods=['POST'])
def handle_data():   
    ProductID = request.form['ProductID']
    FromLocation=request.form['FromLocation']
    ToLocation=request.form['ToLocation']
    productQuantity=request.form['ProductQuantity']

    if "editMovementId" in request.form:
        editMovementId=request.form['editMovementId']
        if FromLocation == ToLocation:
            flash(message='From location and To location cannot be the same',category='danger')
            return redirect('/movements/home')
        freeQty= GetFreeProductQuantity(ProductID)
        if freeQty[0][0] < int(productQuantity):
            currentQty=GetCurrentQty(editMovementId)
            if currentQty[0][0] < int(productQuantity):
                 flash(message='The entered product quantity exceeds the available quantity',category='danger')
                 return redirect('/movements/home')
        
        sql="update productmovement set productid= %s , qty =%s , from_location=%s, to_location=%s where MovementId=%s"
        val = (ProductID,productQuantity, FromLocation,ToLocation,editMovementId)
       
    else:
        if FromLocation == ToLocation:
            flash(message='From location and To location cannot be the same',category='danger')
            return redirect('/movements/home')
        freeqty= GetFreeProductQuantity(ProductID)
        if freeqty[0][0] < int(productQuantity):
            flash(message='The entered product quantity exceeds the available quantity',category='danger')
            return redirect('/movements/home')

        sql = " insert into productmovement  (`MovementId`, `from_location`, `to_location`, `productiD`, `qty`)  VALUES (%s, %s, %s, %s, %s)"
        val = (str(uuid.uuid4()),FromLocation,ToLocation,ProductID,productQuantity)
        flash(message='Movement has been added successfully',category='info')
    mydb=GetDB()
    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect('/movements/home')


