### Generating HTML Responses
### In web applications, particularly those like Flask, it's common to return HTML content directly from your server. This can be used to display information, forms, and other interactive elements to the user.

### Why HTML Responses?
### Returning HTML allows your web server to send not just data but structured content that can be immediately rendered and interacted with by web browsers. It's ideal for providing users with interactive interfaces directly from your server.

### Example of Generating HTML:
### Here’s how you can modify your Flask application to return a simple HTML form dynamically if no score is provided, or display the score if one is validly submitted.

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
        return """
        <html>
            <head><title>Submit Your Score</title></head>
            <body>
                <h1>Score Submission Form</h1>
                <form action="/submit_score" method="get">
                    <input type="text" name="score" required>
                    <input type="submit" value="Submit Score">
                </form>
            </body>
        </html>
        """, 200

    try:
        score = int(score)  # Convert score to an integer
        if score < 0 or score > 100:
            return jsonify({'message': 'Score must be between 0 and 100'}), 400
    except ValueError:
        return jsonify({'message': 'Invalid score, must be an integer'}), 400

    return jsonify({'message': f'Score received: {score}'})

if __name__ == '__main__':
    app.run(debug=True)

### In this version:

### If no score is provided, an HTML form is returned, allowing the user to submit a score.
### If a score is provided and valid, a JSON message is returned (as before).

### Exercise:
### Implement this change in your Flask application and test:

### Accessing the route without a score to see the HTML form.
###Submitting a score through the form to ensure it's processed correctly.

