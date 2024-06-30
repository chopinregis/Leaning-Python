### Handling HTTP Requests with Flask

### What is an HTTP Request?
### An HTTP request is made by a client to a server in the context of a web application. It can be a request for data, a submission of form data, or even a command for the server to do something. Flask handles these requests by mapping URLs to Python functions, allowing specific functions to respond to specific HTTP requests.

### Flask Basics:
### - Routes: In Flask, a route is the URL path to a specific function. When a user visits a URL, Flask executes the associated function and returns a response.
### - Request Object: Flask provides a request object that contains all the data sent by the client. This can include URL parameters, JSON data, and form data.

### example setup:
### To use Flask, you usually set it up in a Python script. Here's a very basic example:

from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


### In this example, when a user visits http://[hostname]/hello, they will receive a response that says "Hello, World!"

### Flask is a web framework that can be used with any web framework. You can use it with any framework, but Flask is the most common.

## Exercise:
## For this exercise, please set up a simple Flask application like the one above on your local machine. You'll need to install Flask if you haven't already. You can do this using pip:

# pip install flask

### Create a new Python file, add the Flask code I provided, and run it. Then, visit http://127.0.0.1:5000/hello in your web browser to see the output. Share with me what you see or if you encounter any issues.

