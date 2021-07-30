from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    text = "this is main index"
    
    return render(request, 'mainApp/index.html', {
        'text': text
    })