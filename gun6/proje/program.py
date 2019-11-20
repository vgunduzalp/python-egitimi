from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    a = 5
    adi  ="veysel"
    return render_template("index.html",sayi=a,ad=adi)

@app.route('/home')
def home():
    data = {
        "ad": "veysel",
        "soyad": "gunduzalp"
    }

    data["yas"] = 21

    print("len",len(data));

    return render_template("home.html",data=data)

@app.route("/uye_detay")
def detay():
    return render_template("uye_detay.html")

@app.route("/anasayfa")
def anasayfa():
    return render_template("anasayfa.html")


if __name__ == "__main__":
    app.run(debug=True)