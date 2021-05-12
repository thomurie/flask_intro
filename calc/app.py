# Put your app in here.

from flask.app import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def use_add():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))

    return str(add(a,b))

@app.route('/sub')
def use_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))

    return str(sub(a,b))
    
@app.route('/mult')
def use_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))

    return str(mult(a,b))

@app.route('/div')
def use_div():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))

    return str(add(a,b))