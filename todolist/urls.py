from django.urls import path
from todolist.views import show_todolist, register, login_user, create_task, mark_done, delete_task, logout_user

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    path("create-task", create_task, name="create_task"),
    path("mark-done/<int:id>", mark_done, name="mark_done"),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
    path("logout/", logout_user, name="logout"),
]