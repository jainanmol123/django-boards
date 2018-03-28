from django.shortcuts import render
from accounts import views as accounts_views
# Create your views here.
def signup(request):
    return render(request,'boards/signup.html')
