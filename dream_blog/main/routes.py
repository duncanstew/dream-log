from flask import render_template, request, Blueprint
from dream_blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    # How to paginate these
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('index.html', posts=posts)

    
@main.route("/resources")
def resources():
    return render_template('resources.html', title='Resources')

@main.route("/trends")
def trends():
    return render_template('trends.html', title='Trends')

@main.route("/animations")
def induction_techniques():
    return render_template('aatest.html', title='Dream')
