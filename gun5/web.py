from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "merhaba"

@app.route('/user/<string:id>')
def user_sayfasi(id):
    print("user calisti")
    return id



if __name__ == "__main__":
    print("main calisti")
    app.run(debug=True)