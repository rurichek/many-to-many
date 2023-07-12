"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    image_url = db.Column (db.String)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.id} {self.first_name} {self.last_name} {self.image_url} >"


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                   primary_key=True,)
                #    autoincrement=True)
    title = db.Column(db.String(10000))
    content = db.Column(db.String(1000))
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now
    )
    user_id = db.Column (
        db.Integer, 
        db.ForeignKey('users.id')) 
    

    def __repr__(self):
        return f"<Post {self.id} {self.title} {self.content} {self.user_id} >"
    
class Tag(db.Model):

    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String, unique=True)   

    posts = db.relationship('Post', secondary="posts_tags", backref="tags")

    def __repr__(self):
        return f"<ID: {self.id} Name: {self.name}>"

class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True, nullable=False)    
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True, nullable=False)  

    def __repr__(self):
        return f"<Post id: {self.post_id} Tag id: {self.tag_id}>"

    
    

    
