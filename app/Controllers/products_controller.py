  
from flask import Blueprint, render_template,flash,url_for,request,redirect
import os
from app.Util.dbUtil import GetData
from app.Util.dbUtil import GetDB
import uuid

template_dir = os.path.abspath('app/views/products')

products_blueprint = Blueprint('products', __name__, template_folder=template_dir,url_prefix='/products/')

@products_blueprint.route('/home')
def index():
    products=GetData('product','productname')
    return render_template('products/index.html',productsList=products)


@products_blueprint.route('/handle_data', methods=['POST'])
def handle_data():
    productName = request.form['productName']
    productQuantity=request.form['productQuantity']

    if "productid" in request.form:
        productid=request.form['productid']
        sql="update product set productname= %s , Quantity =%s where product_id=%s"
        val = (productName,productQuantity,productid)
        flash(message='Product has been updated successfully',category='info')
    else:
        sql = "INSERT INTO product (`product_id`, `ProductName`, `Quantity`) VALUES (%s, %s, %s)"
        val = (str(uuid.uuid4()),productName,productQuantity)
        flash(message='Product has been added successfully',category='info')
    mydb=GetDB()
    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect('/products/home')


