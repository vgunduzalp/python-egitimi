from flask import Flask, render_template, request, redirect
from Db import Db

app = Flask(__name__)

@app.route("/")
def index():
    db = Db()

    sql = """ select * from "gorev" """

    data = db.read_data(sql)

    return render_template("index.html", data=data)

@app.route("/gorev_ekle",methods=["post"])
def gorev_ekle():
    db =Db()
    sql = """ insert into "gorev" ("GorevAdi", "TamamlandiMi")  values (%s, %s) """
    gorev_adi = request.form.get('gorev_aciklama')
    db.execute(sql,(gorev_adi,True))
    return redirect("/")


@app.route("/gorev_sil/<string:id>")
def gorev_sil(id):

    database = Db()
    sql = """ delete from "gorev" where "Id" = %s """
    database.execute(sql,(id,))

    return redirect("/")


@app.route("/gorev_duzenle/<string:id>")
def gorev_duzenle(id):
    database = Db()

    sql = """ select * from "gorev" where "Id" = %s """
    gorevim = database.read_first_data(sql,(id,))

    data = {
        "id" : gorevim[0],
        "gorev_adi" : gorevim[1],
        "tamamlandimi": gorevim[2]
    }
    return render_template("duzenle.html",data= data)

@app.route("/gorev_update",methods=["post"])
def gorev_update():
    tamamlandimi = False
    id = request.form.get('gorev_id')
    gorev_aciklama = request.form.get('gorev_aciklama')
    if request.form.get('tamamlandimi') == "on":
        tamamlandimi = True

    databse = Db()
    sql = """  update "gorev" set "GorevAdi" = %s, "TamamlandiMi" = %s where "Id" = %s  """

    databse.execute(sql,(gorev_aciklama,tamamlandimi,id))

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)