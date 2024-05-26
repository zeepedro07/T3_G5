from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.User import User
from classes.Imovel import Imovel
from classes.Agendamentos import Agendamentos

from classes.userlogin import Userlogin

app = Flask(__name__)

User.read(filename + 'business.db')
Imovel.read(filename + 'business.db')
Agendamentos.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')
prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'ProductFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_subform as gfsubsub
import subs_productFoto as productFotosub
import subs_mapaOrderform as mapasub


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"), usergroup=session.get('users'))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu,usergroup=session.get('users'))

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

       
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)


@app.route("/productform", methods=["post","get"])
def productFoto():
    submenu = request.args.get("subm")
    cname = 'Product'
    return productFotosub.productFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():
    submenu = request.args.get("subm")
    cname = ''
    return mapasub.mapaOrderform(app,cname,submenu)

@app.route("/uc", methods=["post","get"])
def uc():
    return render_template("uc.html", ulogin=session.get("user"),submenu=submenu, usergroup=session.get('users'))


    
if __name__ == '__main__':
    app.run(debug=True,port=6001)
    #app.run()