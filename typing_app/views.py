from django.shortcuts import render, redirect
from login_app.models import User
from django.contrib import messages
from .models import Test, Text
from datetime import datetime
import random
import pygal
import simplejson
# from pygal.graph.public import PublicApi

def typingmaster_home(request):
    if not "user_id" in request.session:
        messages.error(request, "Please, log in")
        return redirect("/")
    return render(request, "home.html")

def test_page(request):
    if not "user_id" in request.session:
        messages.error(request, "Please, log in")
        return redirect("/")
    if not "test_level" in request.POST:
        messages.error(request, "Please, select the difficulty before start!")
        return redirect("/typingmaster")
    text = Text.objects.filter(difficulty = int(request.POST['test_level']))
    context = {
        "text":random.choice(text)
    }
    request.session['text_id'] = context["text"].id
    return render(request, "test.html", context)

def collect_results(request):
    if "cancel" in request.POST:
        return redirect("/typingmaster")
    user = User.objects.get(id = request.session['user_id'])
    text = Text.objects.get(id = request.session['text_id'])
    Test.objects.create(speed = request.POST['final_speed'],
        errors = request.POST['total_errors'],
        accuracy = request.POST['accuracy'],
        user = user,
        text = text)
    return redirect("/typingmaster/results")

def test_results(request):
    if not "user_id" in request.session:
        messages.error(request, "Please, log in")
        return redirect("/")
    user = User.objects.get(id = request.session['user_id'])
    tests = Test.objects.filter(user = user)
    speed_list = []
    date_list = [""]
    stats_list = [user.taken_tests.last().errors, user.taken_tests.last().speed, user.taken_tests.last().accuracy]
    for test in tests:
        speed_list.append(test.speed)
        date_list.append(test.created_at.strftime("%b - %e %H:%M %p"))
    speed_data = simplejson.dumps(speed_list)
    date_data = simplejson.dumps(date_list)
    test_stats = simplejson.dumps(stats_list)
    return render(request, "results.html", {"speed": speed_data, "date": date_data, "stats": test_stats})

def hall_of_fame(request):
    if not "user_id" in request.session:
        messages.error(request, "Please, log in")
        return redirect("/")
    speed_list = []
    accuracy_list = []
    users = User.objects.all()
    for item in users:
        speed_list.append(item.top_speed())
    for item in users:
        accuracy_list.append(item.top_accuracy())
    accuracy_list.sort(key = lambda Test: Test.accuracy, reverse = True)
    speed_list.sort(key = lambda Test: Test.speed, reverse = True)
    context = {
        "tests_by_speed":speed_list,
        "tests_by_accuracy":accuracy_list
    }
    return render(request, "halloffame.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")