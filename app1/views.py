from django.shortcuts import render

def home(request):
    return render(request, 'inicial/pages/home.html')

def about(request):
    return render(request, 'inicial/pages/about.html')

def games(request):
    return render(request, 'inicial/pages/games.html')

def creation(request):
    return render(request, 'inicial/pages/creation.html')

def contact(request):
    return render(request, 'inicial/pages/contact.html')
