from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html',name=name)

@app.route('/page/<int:postID>')
def show_page(postID):
    return render_template('page.html',pageno=postID)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_name',name=name))
    
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/login')
def login():
    return 'Login Page'

@app.route('/home')
def home():
    return 'Home Page'

@app.route('/register')
def register():
    return 'Register Page'




if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
