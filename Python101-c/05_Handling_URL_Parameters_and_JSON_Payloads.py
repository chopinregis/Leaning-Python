### Handling URL Parameters and JSON Payloads

### URL Parameters:
### These are typically used for passing small amounts of data to the server via the URL. They are easily accessible in Flask using request.args.

### JSON Payloads:
### For more complex data or for operations like POST requests where you need to send data securely and invisibly, JSON payloads are used. These can be accessed in Flask using request.get_json().

### Combined Example:
### Let’s write a Flask application that can handle both types of input—URL parameters and JSON payloads. This will closely resemble the initial function you want to build, where a score can be submitted either way.

### Exercise:
### Create a Flask route that accepts a score either as a URL parameter or via a JSON payload and returns a simple message based on the score.

### Exercise:
### Create a Flask route that accepts a score either as a URL parameter or via a JSON payload and returns a simple message based on the score.

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/submit_score', methods=['GET', 'POST'])
def submit_score():
    if request.method == 'GET':
        score = request.args.get('score')
    elif request.method == 'POST':
        data = request.get_json()
        score = data.get('score') if data else None

    if score is None:
        return jsonify({'message': 'No score provided'}), 400

    return jsonify({'message': f'Score received: {score}'})

if __name__ == '__main__':
    app.run(debug=True)

### In this code:

### - GET requests look for a score in the URL parameters.
### - POST requests expect a JSON body with a score.
### The response is JSON-formatted, which is typical for APIs.

### Testing:
### - GET Request: Visit http://127.0.0.1:5000/submit_score?score=85 in your browser.
### -POST Request: Use a tool like Postman or write a simple curl command:

# curl -X POST http://127.0.0.1:5000/submit_score -H "Content-Type: application/json" -d '{"score": "90"}'
# or for powerswell:
# Invoke-WebRequest -Uri http://127.0.0.1:5000/submit_score -Method POST -ContentType "application/json" -Body '{"score":"90"}'
