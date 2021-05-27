from django.db import models
from datetime import date, datetime
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        
        if(len(post_data['first_name']) < 2):
            errors['first_name'] = "First name must be atleast 2 characters"
        if(len(post_data['last_name']) < 2):
            errors['last_name'] = "Last name must be atleast 2 characters"
        

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"

        user = User.objects.filter(email=post_data['email'])
        if user:
            errors['email'] = "Email already used!"

        if(len(post_data['password']) > 64 or len(post_data['password']) < 8):
            errors['password'] = "Password must be 64 characters or less, and more than 8"
        if(post_data['confirm'] != post_data['password']):
            errors['password'] = "Passwords must match"

            
        return errors

class RestaurantManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if(len(post_data['name']) < 2):
            errors['name'] = "Your name must be at least 2 characters"

        if(len(post_data['address']) < 2):
            errors['address'] = "Your address must be at least 2 characters"

        if(len(post_data['phone_number']) < 2):
            errors['phone_number'] = "Your phone number must be at least 2 characters"

        return errors

class ReviewManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}

        if(len(post_data['content']) < 2):
            errors['content'] = "Your review must be at least 2 characters"



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    # reviews = a list of all the user's reviews
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

class Restaurant(models.Model):
    creator = models.ForeignKey(User, related_name="restaurants", on_delete = models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    # reviews = a list of all the restaurant's reviews
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RestaurantManager()

class Review(models.Model):
    content = models.TextField()
    restaurant = models.ForeignKey(Restaurant, related_name="reviews", on_delete = models.CASCADE)
    reviewer = models.ForeignKey(User, related_name="reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()