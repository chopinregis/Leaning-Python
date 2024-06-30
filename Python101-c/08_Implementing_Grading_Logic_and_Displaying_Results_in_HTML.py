### Implementing Grading Logic and Displaying Results in HTML
### In this step, you'll implement the grading logic that determines a letter grade based on the score and then displays this grade using HTML.

### Grading Logic:
### The grading logic is straightforward:

### - 90 and above is an 'A'
### - 80 to 89 is a 'B'
### - 70 to 79 is a 'C'
### - 60 to 69 is a 'D'
### - Below 60 is an 'F'

### Example of Implementation:
### Here's how you might integrate the grading logic into your Flask application and display the results:

from flask import Flask, request
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
        score = int(score)
        if score < 0 or score > 100:
            return 'Score must be between 0 and 100.', 400
    except ValueError:
        return 'Invalid score, must be an integer.', 400

    # Grading logic
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # HTML response with the grade
    return f"""
    <html>
        <head><title>Grade Result</title></head>
        <body>
            <h1>Your grade is: {grade}</h1>
            <button onclick="window.location='/submit_score';">Try Again</button>
        </body>
    </html>
    """, 200

if __name__ == '__main__':
    app.run(debug=True)

### In this implementation:
### The grading logic determines the letter grade based on the score.
### An HTML response displays the grade and provides a button to submit a new score.

### Exercise:
### Implement this grading logic in your Flask application.
### Test the functionality by submitting various scores to ensure the correct grade is displayed.