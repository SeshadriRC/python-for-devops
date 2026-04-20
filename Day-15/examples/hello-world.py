from flask import Flask    # importing Flask module from the flask package

app = Flask(__name__)  # Its a common line, every flask program will have this. we are creating a flask app instance

@app.route('/')        # A decorator is a shortcut that adds extra functionality to a function using @ syntax. It tells Flask: when someone visits /, run the hello_world() function.
def hello_world():
    return 'Hello, World!'
    
    app.run("0.0.0.0")     # Run on the local machine ip address, by default flask application will run on port 5000
