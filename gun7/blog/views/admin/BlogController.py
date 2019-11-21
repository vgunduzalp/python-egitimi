from flask import Blueprint, render_template

blog = Blueprint('blog',__name__,
                 url_prefix="/admin/blog")


@blog.route("/index")
def index():
    return render_template("admin/blog/index.html")