from flask import Flask, request, make_response, redirect, url_for

stu_information = {"admin": 123456
app = Flask(__name__)


@app.route('/')
def index():
    """主页"""
    return '''
    <a href="/">Home</a>
    <a href="/blogs">Blogs</a>
    <a href="/about">About Me</a>
    <h1>Hello, this is Russell's site!</h1>
    <h3>You are not logged in, please <a href="/login">CLICK HERE</a> to log in.</h3>
    '''


@app.route('/login')
def login():
    """登录"""
    return '''
    <a href="/">Home</a>
    <a href="/blogs">Blogs</a>
    <a href="/about">About Me</a>
    <form action="/info" method="post">
    用户名：<input type="text", name="username"/>
    <br/>
    密&nbsp;&nbsp;&nbsp;码：<input style="margin-left:2px" type="password", name="pwd"/>
    <button>登录</button>
    </form>
    '''


@app.route('/blogs')
def blogs():
    """blogs页面"""
    return '''
    <a href="/">Home</a>
    <a href="/blogs">Blogs</a>
    <a href="/about">About Me</a>
    <h1>This is my blogs.</h1>
    '''


@app.route('/about')
def about():
    """关于我的页面"""
    return '''
    <a href="/">Home</a>
    <a href="/blogs">Blogs</a>
    <a href="/about">About Me</a>
    <h1>I am a coding teacher. Call me: 010-101010101.</h1>
    '''


@app.route('/info', methods=["post"])
def get_info():
    """处理用户登录"""
    about_url = url_for('about')
    login_url = url_for('login')
    user = request.form.get("username")
    pwd = int(request.form.get("pwd"))
    for username, password in stu_information.items():
        if user == username and pwd == password:
            return redirect(about_url)
        else:
            return redirect(login_url)


if __name__ == '__main__':
    app.run(debug=True)
