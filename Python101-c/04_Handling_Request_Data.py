### Handling Request Data
### Now that you've got a basic Flask app running, the next step is to learn how to handle incoming data through the Flask request object. This will be crucial for your grading function which needs to process scores either from URL query parameters or JSON payload.

### Flask request Object:
### The request object in Flask contains all the information sent by the client. This includes:
###     - URL parameters (accessed via request.args)
###     - JSON payloads (accessed via request.get_json())


### Exercise:
### Modify your Flask application to accept a name parameter via the URL query string and return a personalized greeting. Here’s a simple example of what the code would look like:

from flask import Flask, request
app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)


### Run this code, and test it by visiting http://127.0.0.1:5000/greet?name=YourName in your browser, replacing YourName with any name you choose.

