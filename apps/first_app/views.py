from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string

# the index function is called when root is visited

def index(request):

    if 'count' not in request.session:
        request.session['count']=0
        request.session['word']=0
        request.session['color']=0

    return render(request, 'session_word/pages.html')

def process(request, methods=['POST']):
    request.session['word']+=request.POST['word']
    request.session['color']+=request.POST['color']
    request.session['count'] +=1
    return redirect('/')

