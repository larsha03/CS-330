from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
import math

app = Flask(__name__)


def is_prime(n: int) -> bool:
<<<<<<< HEAD
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
=======
    raise NotImplementedError


def get_n_primes(n: int) -> list:
>>>>>>> 560c2c54b62c4610235f2cd20c1ab3e25ae14f6f
    raise NotImplementedError


@app.route('/')
def index():
<<<<<<< HEAD
    print(request.args)
    if request.method == 'GET':
        return render_template('ask.html')
    raise NotImplementedError

@app.route('/<int:n>',methods=['GET','POST'])
def get_primes(n):
    x= True
    for i in range(2, n):
        if n%i == 0:
            x = False
            break
    if x:
        return 'Number is prime: ' +  str(n)
    else:
        return 'Number is not prime: ' +  str(n)
    
    raise NotImplementedError

@app.route('/ask/num', methods=['GET','POST'])
def ask_a_number():
    if request.method == 'GET':
        return render_template('ask.html')    
=======
    raise NotImplementedError

@app.route('/<int:n>')
def get_primes(n):
    raise NotImplementedError

@app.route('/ask')
def ask_a_number():
>>>>>>> 560c2c54b62c4610235f2cd20c1ab3e25ae14f6f
    raise NotImplementedError


if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run()
>>>>>>> 560c2c54b62c4610235f2cd20c1ab3e25ae14f6f
