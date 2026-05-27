from django .urls import path,include
from django.urls import path
from .views import home_page,profile_page,contact_page,grade_page
urlpatterns = [
    path("home/",home_page),
    path("profile/",profile_page),
    path("contact/",contact_page),
    path("grade/", grade_page),
]