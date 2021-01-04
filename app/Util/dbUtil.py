
import mysql.connector

def GetDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_management"
    )
    return mydb

def GetData(tableName,orderByColumn):
    d=GetDB()
    mycursor=d.cursor()
    sql='SELECT * FROM {table_name} ORDER BY {order_By_Column}'.format(table_name=tableName,order_By_Column=orderByColumn)
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetMovements():
    d=GetDB()
    mycursor=d.cursor()
    sql="select pm.MovementId , pm.timestamp, (SELECT locationname from location l1 where l1.Location_id=pm.from_location) 'From_Location',(SELECT locationname from location l2 where l2.Location_id=pm.to_location) 'To_Location' ,(SELECT productname from product p where p.product_id=pm.productiD) 'Productname',pm.qty from productmovement pm ORDER by timestamp"
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetProductLocations(productID):
    d=GetDB()
    mycursor=d.cursor()
    sql="SELECT  distinct (select l.LocationName from location l where l.Location_id=pm.from_location) 'test', pm.from_location FROM productmovement pm WHERE pm.productiD='{product_id}' and length(from_location)>0".format(product_id=productID)
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetProductQuantity(productID):
    d=GetDB()
    mycursor=d.cursor()
    sql="SELECT Quantity from product where product_iD='{product_id}'".format(product_id=productID)
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetFreeProductQuantity(productID):
    d=GetDB()
    mycursor=d.cursor()
    sql="SELECT IFNULL(cast(quantity - sum(qty) as int),(select Quantity from product where product_id='{product_id}')) as num FROM product p , productmovement pm WHERE pm.productiD=p.product_id and pm.productiD='{product_id}'".format(product_id=productID)
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetCurrentQty(editMovementId):
    d=GetDB()
    mycursor=d.cursor()
    sql="SELECT qty from  productmovement pm WHERE pm.MovementId='{movement_Id}'".format(movement_Id=editMovementId)
    mycursor.execute(sql)
    return mycursor.fetchall()

def GetReport():
    d=GetDB()
    mycursor=d.cursor()
    sql="SELECT (select productname from product p WHERE p.product_id=pm.productiD) 'productname' ,(select locationname from location l where l.Location_id= pm.from_location) 'locationname',sum(qty) 'qty' FROM productmovement pm GROUP by pm.productiD,pm.from_location order by pm.productid"
    mycursor.execute(sql)
    return mycursor.fetchall()


