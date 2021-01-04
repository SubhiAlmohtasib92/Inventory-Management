from flask import Flask,redirect,url_for,render_template
from app.Controllers.products_controller import products_blueprint
from app.Controllers.locations_controller import locations_blueprint
from app.Controllers.productmovement import movements_blueprint
import os
from app.Util.dbUtil import GetReport

template_dir = os.path.abspath('app/views')
assets_dir = os.path.abspath('app/assets')
app= Flask(__name__,template_folder=template_dir,static_folder=assets_dir)
app.register_blueprint(products_blueprint)
app.register_blueprint(movements_blueprint)
app.register_blueprint(locations_blueprint)
app.config['SECRET_KEY'] = 'Web-Inventory-Secret-Key'    

@app.route('/')
def home():
    reportData=GetReport()
    return render_template('homepage/index.html',report=reportData)

@app.route('/<name>/')
def test(name):
   return redirect(url_for('{page_name}.index'.format(page_name=name)))

@app.errorhandler(404)
def not_found():
     return redirect(url_for('home'))

app.run()