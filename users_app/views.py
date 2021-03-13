from users_app.models import Users
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    context = {
        "user_list": Users.objects.all()
    }
    return render(request, "main.html", context)

def process(request):
    if request.method == "POST":
        first = request.POST["first"]
        last = request.POST["last"]
        email = request.POST["email"]
        age = request.POST["age"]

        Users.objects.create(first_name=first, last_name=last, email=email, age=age)

    return redirect('/')





        
