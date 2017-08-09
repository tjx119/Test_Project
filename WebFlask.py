# -*- coding: UTF-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
# 显示用户的名称
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
# 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.run()

@property
def aaa():
    pass

@aaa.setter