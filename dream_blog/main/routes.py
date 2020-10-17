from flask import render_template, request, Blueprint
from dream_blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    # How to paginate these
    # Options will be 'New, Best'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('posts.html', posts=posts)

@main.route("/trending")
def trending():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.upvotes.desc()).paginate(page=page, per_page=6)
    return render_template('posts.html', posts=posts)

    
@main.route("/resources")
def resources():
    return render_template('resources.html', title='Resources')

@main.route("/trends")
def trends():
    return render_template('trends.html', title='Trends')

@main.route("/induction_techniques")
def induction_techniques():
    return render_template('induction_techniques.html', title='Dream')

@main.route("/books")
def books():
    return render_template('books.html', title='Books')


@main.route("/dreamrecall")
def dreamrecall():
    return render_template('dreamrecall.html', title='Books')