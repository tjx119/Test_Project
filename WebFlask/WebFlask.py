# -*- coding: UTF-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Web!"

@app.route('/user/<username>')
def show_user_profile(username):
# 显示用户的名称
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
# 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return "%d + %d = %d" % (a, b, a + b)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug = True)
