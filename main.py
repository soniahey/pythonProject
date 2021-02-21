from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run()

def print_hi(name):
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Python!')
