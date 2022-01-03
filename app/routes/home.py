from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')

@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = (
  db
    .query(Post)
    .order_by(Post.created_at.desc())
    .all()
)

  return render_template(
  'homepage.html',
  posts=posts,
  loggedIn=session.get('loggedIn')
)
# The get_db() function returns a session connection that's tied to this route's context. 
# We then use the query() method on the connection object to query the Post model for all posts in descending order, and we save the results in the posts variable.  

@bp.route('/login')

def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
  'single-post.html',
  post=post,
  loggedIn=session.get('loggedIn')
)
# This time, we use the filter() method on the connection object to specify the SQL WHERE clause, and we end by using the one() method instead of all(). 
# We then pass the single post object to the single-post.html template. 
# Once the template is rendered and the response sent, the context for this route terminates, and the teardown function closes the database connection.  

def single(id):
  return render_template('single-post.html')