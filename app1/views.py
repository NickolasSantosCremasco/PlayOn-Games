from django.shortcuts import render

def home(request):
    return render(request, 'inicial/pages/home.html')