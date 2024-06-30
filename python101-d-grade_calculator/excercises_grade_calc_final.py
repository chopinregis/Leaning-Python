from flask import Flask, request, render_template_string

app = Flask(__name__)

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

@app.route('/grades', methods=['GET', 'POST'])
def grades():
    if request.method == 'POST':
        score = request.form.get('score')
        if score is not None:
            try:
                score = int(score)
                grade = calculate_grade(score)
                return render_template_string("""
                    <h1>Your grade is: {{grade}}</h1>
                    <a href="/grades">Calculate another grade</a>
                """, grade=grade)
            except ValueError:
                return "Invalid input. Please enter a number.", 400
    
    # If it's a GET request or if no score was provided in POST
    return render_template_string("""
        <h1>Grade Calculator</h1>
        <form method="post">
            <input type="number" name="score" placeholder="Enter score">
            <input type="submit" value="Calculate Grade">
        </form>
    """)

if __name__ == '__main__':
    app.run(debug=True)