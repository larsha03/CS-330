from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
import math

app = Flask(__name__)


def is_prime(n: int) -> bool:
    x = True 
    for i in range(2, n):
        if n%i == 0:
            x = False
            break
    if x:
        print("number is prime")
        return n
    else:
        print("number is not prime")
        return n
    raise NotImplementedError

def get_n_primes(n: int) -> list:
    a = is_prime(n)
    for i in range(1, a+1):
        is_prime(i)
    return n
    raise NotImplementedError


@app.route('/', methods=['GET','POST'])
def index():
    print(request.args)
    if request.method == 'GET':
        num = request.cookies.get('number')
        if num:
            return render_template('prime_table.html', number=num)
        else:
            return render_template('ask.html')
    else:
        response = make_response(redirect(url_for('prime_table.html')))

        if request.form.get('number'):
            response.set_cookie('number', '', expires=0)
        else:
            num = request.form.get('number')
            response.set_cookie('number', num)

        return response

    raise NotImplementedError

@app.route('/<int:n>', methods=['GET'])
def get_primes():    
    return 'number available:' + str(n)

    #raise NotImplementedError

@app.route('/ask/num')
def ask_a_number():
    pass

    #raise NotImplementedError


if __name__ == '__main__':
    app.run()