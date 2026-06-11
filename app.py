from flask import Flask, render_template, request

app = Flask(__name__)

available_rooms = ["A101", "A102", "A103", "B201", "B202", "B203"]

@app.route('/')
def home():
    return render_template('index.html', rooms=available_rooms)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    student_id = request.form['student_id']
    room = request.form['room']

    return render_template('success.html', name=name, student_id=student_id, room=room)

if __name__ == '__main__':
    app.run(debug=True)