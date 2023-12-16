"""
@FileName：test_left_right_join.py
@Description：
@Author：shenxinyuan
@Time：2023/12/13
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 左外连接
left_outer_join_query = db.session.query(User, Post).outerjoin(Post, User.id == Post.user_id)

# 右外连接
right_outer_join_query = db.session.query(User, Post).outerjoin(Post, User.id == Post.user_id)

# 全外连接
full_outer_join_query = db.session.query(User, Post).outerjoin(Post, User.id == Post.user_id, full=True)

# 内连接查询
inner_join_query = db.session.query(User, Post).join(Post)
