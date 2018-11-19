from django.shortcuts import render, HttpResponse
#from django.views.static.serve()

# Create your views here.

def home(request):
    return render(request, 'chat.html')
