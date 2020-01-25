
from django.shortcuts import render
from webtestapp.forms import TestForm

def index(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'Bashi',
    'form':TestForm(),
    'insert_forms':'初期値',
    }
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)

    return render(request,'webtestapp/index.html',my_dict)


