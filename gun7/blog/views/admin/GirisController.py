from flask import Blueprint, render_template, redirect, request, session
import hashlib
from utils.Db import Db



giris = Blueprint('giris',__name__,
                 url_prefix="/admin/giris")


@giris.route("/")
def index():
    return render_template("admin/giris/index.html",hata=False)

@giris.route("/cikis")
def cikis():
    session["FullName"] = None
    session["isLogin"] = None
    return redirect("/admin/giris")


@giris.route("/login",methods=["POST","GET"])
def login():
    email = request.form.get("email")
    sifre = request.form.get("sifre")

    sifre_hash = hashlib.md5(sifre.encode()).hexdigest()

    databse = Db()

    sql = """ select * from "User" where "Email"=%s and "Password"=%s """

    find = databse.read_first_data(sql,(email,sifre_hash))

    if find is None:
        return render_template("admin/giris/index.html",hata=True)
    print(find)
    session["FullName"] = find[3]
    session["isLogin"] = True

    return redirect("/admin/uye/index")


