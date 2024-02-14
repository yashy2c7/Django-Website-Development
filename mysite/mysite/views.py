from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def shop(request):
    return render(request, "shop.html")


def test(request):
    data = {
        "Name": "Yash Chauhan",
        "Course": "Btech ",
        "Year": "3rd year",
        "description": "He is a good software developer and Website developer",
        "skills": ["PHP", "java", "Python "],
        "clist":
          [
            {'name':'pradeep','phone':9269698122},
            {'name':'testing','phone':909696981225}
          ]
    }
    return render(request, "testing.html", data)
 