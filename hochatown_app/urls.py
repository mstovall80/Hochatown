from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("main", views.main),
    path("dinning", views.dinning),
    path("restaurant_review/<int:restaurant_id>", views.restaurant_review),
    path("display_restaurant", views.display_restaurant),
    path("add_restaurant", views.add_restaurant),
    path("added_rev", views.added_rev),
    path("delete_rev/<int:review_id>", views.delete_rev),
    path("lake", views.lake), 
    path("cabin", views.cabin),
    path("boating", views.boating),
    path("fishing", views.fishing),
    path("hiking", views.hiking),
    path("rentals", views.rentals),
    path("logout", views.logout)
]