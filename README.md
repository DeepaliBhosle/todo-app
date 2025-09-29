#  Flask To-Do App

A simple To-Do web application built using **Flask**, deployed with **Render**.

##  Features
- Add and delete tasks
- Tasks stored in `tasks.json`
- Clean Bootstrap UI
- Deployable with Docker or Render

##  Tech Stack
- Python (Flask)
- HTML + Bootstrap
- Gunicorn (for production)

##  How to Run Locally
```bash
git clone https://github.com/DeepaliBhosle/todo-app.git
cd todo-app
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py

##  Live Demo
[Click Here](https://todo-app-ha60.onrender.com/)
