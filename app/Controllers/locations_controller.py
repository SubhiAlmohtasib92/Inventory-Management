from flask import Blueprint, render_template,flash,url_for,request,redirect
import os
from app.Util.dbUtil import GetData
from app.Util.dbUtil import GetDB
import uuid

template_dir = os.path.abspath('app/views/locations/')
locations_blueprint = Blueprint('locations', __name__, template_folder=template_dir,url_prefix='/locations/')

@locations_blueprint.route('/home')
def index():
    locations=GetData('location','adddate')
    return render_template('locations/index.html',locationList=locations)

@locations_blueprint.route('/handle_data', methods=['POST'])
def handle_data():
    locationName = request.form['locationName']
    if "locationID" in request.form:
        locationID=request.form['locationID']
        sql="update location set locationName= %s where location_id=%s"
        val = (locationName,locationID)
        flash(message='Location has been updated successfully',category='info')
    else:
        sql = "INSERT INTO location (`location_id`, `locationName`) VALUES (%s, %s)"
        val = (str(uuid.uuid4()),locationName)
        flash(message='Location has been added successfully',category='info')
    mydb=GetDB()
    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect('/locations/home')