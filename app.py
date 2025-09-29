from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    tasks = load_tasks()
    tasks.append({"task": task_text, "completed": False})
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

