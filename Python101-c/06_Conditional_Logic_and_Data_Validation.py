### Conditional Logic and Data Validation

### In any application that processes input data, it's essential to include conditional logic and data validation. This ensures that the data received is in the expected format and falls within the expected range or meets specific criteria.

### Conditional Logic:
### Conditional logic refers to using if, elif, and else statements to execute different blocks of code based on certain conditions. This is crucial for making decisions within your programs.

### Data Validation:
### This involves checking the data for correctness, completeness, and adherence to the expected format before processing it. It's essential for preventing errors and ensuring reliable app behavior.

### Example Exercise:
### Modify your Flask application to validate the score input. The score should be an integer between 0 and 100. If it's not, the application should return an appropriate error message.

### Here's how you might extend the previous example to include this:

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

    try:
        score = int(score)  # Convert score to an integer
        if score < 0 or score > 100:
            return jsonify({'message': 'Score must be between 0 and 100'}), 400
    except ValueError:
        return jsonify({'message': 'Invalid score, must be an integer'}), 400

    return jsonify({'message': f'Score received: {score}'})

if __name__ == '__main__':
    app.run(debug=True)

"""
In this code:
    - We try to convert the score to an integer using int(score).
    - If this fails (e.g., if the score is not a valid integer), a ValueError is caught, and an error message is returned.
    - If the score is an integer but not in the range 0-100, another error message is provided.

Testing:
    - Test with a valid score in the correct range to see the success message.
    - Test with a non-integer score and a score outside the valid range to see the respective error messages.
"""
