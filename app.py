from flask import Flask, render_template, request

app = Flask(__name__)
tasks = [
    "Buy groceries",
    "Cleaning",
    "Take out the trash",
]


@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return render_template('home.html', tasks=tasks)


@app.route('/delete', methods=['POST'])
def delete_task():
    task = request.form.get('task')
    if task in tasks:
        tasks.remove(task)
    return render_template('home.html', tasks=tasks)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
