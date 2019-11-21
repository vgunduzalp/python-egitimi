from flask import Blueprint, render_template

blog = Blueprint('anasayfa',__name__,
                 url_prefix="/anasayfa")


@blog.route("/")
def index():
    return render_template("/index.html")