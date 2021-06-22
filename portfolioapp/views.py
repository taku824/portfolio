from django.shortcuts import render

# Create your views here.
def top(request):
    return render(request, 'top.html')
def index(request):
    return render(request, 'about.html')
def show(request):
    return render(request, 'about.html')
    
