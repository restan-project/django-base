
from django.shortcuts import render
from webtestapp.forms import TestForm


def index(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'Bashi',
    }
    return render(request,'webtestapp/index.html',my_dict)


