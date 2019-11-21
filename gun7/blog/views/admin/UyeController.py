from flask import Blueprint, render_template, session, redirect,request
from utils.Db import Db
import hashlib

uyeler = Blueprint('uyeler',
                   __name__,
                   url_prefix="/admin/uye")


@uyeler.route("/index")
def index():
    databse = Db()
    sql = """ select * from "User" """
    data = databse.read_data(sql);

    return render_template("admin/uye/index.html",data=data)


@uyeler.route('/ekle', defaults={'id': None})
@uyeler.route('/ekle/<string:id>')
def ekle(id):

    if id is not None:
        databse = Db()
        sql = """ select * from "User" where "Id" = %s """
        data = databse.read_first_data(sql,(id,))
        print(data)

        return render_template("admin/uye/ekle.html",data=data)

    return render_template("admin/uye/ekle.html",data=None)


@uyeler.route('/save',methods=["POST"])
def save():
    fullName = request.form.get("FullName")
    id = request.form.get("Id")
    email = request.form.get("Email")
    password = request.form.get("Password")

    database = Db()

    sql  = ""
    if id is None:
        sql = """ insert into "User" ("Email","Password","FullName") values (%s,%s,%s) """
        sifre_hash = hashlib.md5(password.encode()).hexdigest()
        database.execute(sql,(email,sifre_hash,fullName))
    else:
        sql = """ update "User" set "FullName"=%s, "Email"=%s """
        params= (fullName,email,id)
        if password != '':
            sifre_hash = hashlib.md5(password.encode()).hexdigest()
            sql += """, "Password"=%s """
            params = (fullName,email,sifre_hash,id)

        sql += """ where "Id" = %s"""

        database.execute(sql,params)

    return redirect("/admin/uye/index")

@uyeler.route('/sil/<string:id>')
def sil(id):
    database = Db()
    sql = """ delete from "User" where "Id"=%s """
    database.execute(sql, (id,))
    return redirect("/admin/uye/index")