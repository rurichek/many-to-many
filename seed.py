"""Seed filet o make sample data for db."""

from models import User, Post, Tag, PostTag, db
from app import app
import datetime

# Create all tables
db.drop_all()
db.create_all()


u1 = User(first_name='Timour', last_name='H', image_url="https://wallpapers-clan.com/wp-content/uploads/2023/05/cool-pfp-02.jpg")
u2 = User(first_name='Sam', last_name='L', image_url="https://64.media.tumblr.com/b95661c0c2183d8aa60837e556e91c0a/570cef43590b36ff-ba/s640x960/8590baafc6601fbb65d269a790a55a561df4ca82.png")
u3 = User(first_name='Jake', last_name='S', image_url="https://www.asiamediajournal.com/wp-content/uploads/2022/11/Spongebob-PFP-1200x1202.jpg")

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()

p1 = Post(title = "My post", content="This is my first post", user_id=1)
p2 = Post(title = "New post", content="Hey all! I am new here!", user_id=2)
p3 = Post(title = "Silly post", content="This is me!", user_id=1)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()

t1 = Tag(name='fun')
t2 = Tag(name='surprising')
t3 = Tag(name='interesting')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.commit()

pt1 = PostTag(post_id=p1.id, tag_id=t1.id)
pt2 = PostTag(post_id=p2.id, tag_id=t2.id)
pt3 = PostTag(post_id=p3.id, tag_id=t3.id)

db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.commit()





