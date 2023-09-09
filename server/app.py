#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>') 
def print_string(text):
    print(text)
    return f'{text}'

@app.route('/count/<int:n>')
def count(n):
    numbers = range(n)
    count = ''
    for num in numbers:
        count += str(num) + '\n'
    return count



@app.route('/math/<int:a>/<operation>/<int:b>')
def math_operations(a, operation, b):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == 'div':
        result = a / b
    elif operation == '%':
        result = a % b
    else:
        return "Invalid operation"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
