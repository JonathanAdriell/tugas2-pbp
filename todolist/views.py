from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/todolist/login/")
def show_todolist(request):

    context = {
        "username": request.user,
        # "todolist": Task.objects.filter(user=request.user)
    }
    return render(request, "todolist.html", context)  # return response


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("todolist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            # ini akan ditampilkan di HTML saat pengguna salah masukin username atau password
            messages.info(request, "Username atau Password salah!")
    context = {}
    return render(request, "login.html", context)


@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            date=datetime.date.today(),
            title=title,
            description=description
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))

    return render(request, "create.html")


@login_required(login_url="/todolist/login/")
def mark_done(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not task.is_finished
    task.save()

    # return response
    return HttpResponseRedirect(reverse("todolist:show_todolist"))


@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()

    # return response
    return HttpResponseRedirect(reverse("todolist:show_todolist"))


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login"))
    response.delete_cookie("last_login")
    return response


@login_required(login_url="/todolist/login/")
def show_json(request):  # get data in JSON
    todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")


@csrf_exempt
def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "title": task.title,
                    "description": task.description,
                    "is_finished": task.is_finished,
                    "date": task.date,
                },
            },
            status=200,
        )
