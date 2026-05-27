from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"home.html")
def profile_page(request,):
    return render(request, "profile.html", {"name": "amit", "email": "amit@gmail.com", "role": "admin", "user_data": [
        {"name": "lulu", "email": "lulu@gmail.com"},
        {"name": "chuchu", "email": "chuchu@gmail.com"},
        {"name": "coco", "email": "coco@gmail.com"}

    ]})

def contact_page(request):
        return render(request, "contact.html", {"range": range(0, 10)})
def grade_page(request):
    return render(request,"grade.html",{"marks":20,"role":"marks"})


