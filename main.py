from flask import Flask
from flask_restplus import Resource, Api

# Flask App initialization
app = Flask(__name__)

api = Api(app, version='1.0', title='API title',
          description='API description',
          )

nspace = api.namespace('custom', description='API namespace')

# SWAGGER_UI_DOC_EXPANSION
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

@app.route("/")
def hello():
    return "Hello World!"

app.run()

def print_hi(name):
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Python!')

