from flask import Flask, render_template

app = Flask(__name__)

# Sample data for office chairs
office_chairs = [
    {"id": 1, "name": "Executive Chair", "price": 199.99},
    {"id": 2, "name": "Task Chair", "price": 99.99},
    {"id": 3, "name": "Mesh Chair", "price": 149.99},
    # Add more chair data as needed
]

@app.route('/')
def index():
    return render_template('index.html', chairs=office_chairs)

if __name__ == '__main__':
    app.run(debug=True)
