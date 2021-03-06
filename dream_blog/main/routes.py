from flask import render_template, request, Blueprint
from dream_blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')

@main.route("/posts")
def posts():
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
    return render_template('induction_techniques.html', title='Induction')

@main.route("/books")
def books():
    return render_template('books.html', title='Books')


@main.route("/dreamrecall")
def dreamrecall():
    return render_template('dreamrecall.html', title='Dream Recall')

@main.route("/realitytesting")
def realitytesting():
    return render_template('realitytesting.html', title='Reality')

@main.route("/research")
def research():
    return render_template('research.html', title='Research')
    
@main.route("/technology")
def technology():
    return render_template('technology.html', title='Technology')