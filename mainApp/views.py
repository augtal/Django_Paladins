from django.shortcuts import render, redirect
from .services import insertToDatabase



# Create your views here.

def index(request):
        data = 0
        message = " "
        
        data, message = insertToDatabase()
        
        text = "this is main index"
        
        return render(request, 'mainApp/index.html', {
            'text': text,
            'champs': data,
            'message': message
        })