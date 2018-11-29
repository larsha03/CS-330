from flask import Flask, render_template, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET','POST'])
def index():
   if 'username' in session:
       return render_template('index.html', username=escape(session['username']))
   else:
       return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect(url_for('index'))

@app.route('/logout', methods=['GET'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run