from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    this_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
    request.session['user_id'] = this_user.id
    return redirect('/')

def login(request):
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/main')

            messages.error(request, "Invalid login")

            return redirect('/')    

def main(request):

    context={
    "user": User.objects.get(id=request.session['user_id']),
    "reviews": Review.objects.all()
    }
    return render(request, "main.html", context)

def lake(request):
    return render(request, "lake.html")

def boating(request):
    return render(request, "boating.html")

def fishing(request):
    return render(request, "fishing.html")

def hiking(request):
    return render(request, "hiking.html")

def cabin(request):
    return render(request, "cabin.html")

def dinning(request):
    return render(request, "dinning.html" )

def rentals(request):
    return render(request, "rentals.html")

def add_restaurant(request ):
    context={
    "user": User.objects.get(id=request.session['user_id']),
    "restaurants": Restaurant.objects.all()
    }
    return render(request, "restaurant.html", context)

def display_restaurant(request):
    this_user = User.objects.get(id=request.session['user_id'])
    this_restaurant = Restaurant.objects.create(creator= this_user, name=request.POST['name'], address=request.POST['address'], phone_number=request.POST['phone_number'])
    return redirect("/add_restaurant")


def restaurant_review(request, restaurant_id):
    user =  User.objects.get(id=request.session['user_id'])
    context={
    "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, "restaurant_review.html", context)

def added_rev(request):
    this_user = User.objects.get(id=request.session['user_id'])
    this_review = Review.objects.create(
        reviewer = this_user, 
        content = request.POST['review'], 
        restaurant = Restaurant.objects.get(id = request.POST['restaurant_id']))
    return redirect('/main')

def delete_rev(request, review_id):
    review_delete = Review.objects.get(id=review_id) 
    review_delete.delete()
    return redirect('/main')

def logout(request):
    if "user_id" not in request.session:
        return redirect('/')
    del request.session['user_id']
    return redirect("/")