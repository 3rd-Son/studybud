from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Let's Learn Python"},
#     {"id": 2, "name": "Let's Learn Rust"},
#     {"id": 3, "name": "Let's Go"},
# ]


def home(request):
    return render(request, "base/home.html")


def room(request, pk):
    return render(request, "base/room.html")
