# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_login.py

"""""

from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin


def login():    
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),usergroup=session.get('users'),resul = "")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('users'))

def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        session['users']=Userlogin.obj[user].usergroup
        return render_template("index.html", ulogin=session.get("user"),usergroup=session.get('users'))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),usergroup=session.get('users'),resul = resul)



