from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_user():
    return '330'

if __name__ == 'main':
    app.run()