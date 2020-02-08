
from django.shortcuts import render
from webtestapp.forms import TestForm
from django.http import HttpResponse


def index(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'Bashi',
    }
    return render(request,'webtestapp/index.html',my_dict)

def api_test(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'name',
    }
    return render(request,'webtestapp/index.html',my_dict)

def detail(request):
    return HttpResponse("You're looking at question %s.")


