from flask import (
    Flask,
    request,
    render_template
)
import requests as pyrequests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/tasks")
def list_tasks():
    response = pyrequests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", code=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/")
def task_detail(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = pyrequests.get(url)
    if response.status_code == 200:
        single_task = response.json().get("task")
        return render_template("detail.html", task=single_task)
    return (
        render_template("error.html", code=response.status_code),
        response.status_code
    )

@app.get("/tasks/new/")
def new_form():
    return render_template("new.html")

@app.post("/tasks/new/")
def create_task():
    task_data = request.form
    response = pyrequests.post(BACKEND_URL, json=task_data)
    if response.status_code == 204:
        return render_template("success.html", msg="Creation successful")
    return (
        render_template("error.html", code=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/edit/")
def edit_form(pk):
    # This function is intended to support auto-populating the edit form
    url = "%s/%s" % (BACKEND_URL, pk)
    response = pyrequests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task")
        return render_template("edit.html", task=task_data)
    return (
        render_template("error.html", code=response.status_code),
        response.status_code
    )

@app.post("/tasks/<int:pk>/edit/")
def edit_task(pk):
    # this is a challenge to be completed by students based off
    # of the previous one (the create_task function).
    # Remove pass below when you're done.
    pass
