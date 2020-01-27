
from django.shortcuts import render
from webtestapp.forms import TestForm
from firebase import firebase

firebase = firebase.FirebaseApplication('https://rezo-sandbox.firebaseio.com', None)

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

    result = firebase.post('/products', "{'id': '1'}, {'name': 'orange'}, {'price': '50'}")
    result = firebase.post('/products', "{'id': '2'}, {'name': 'apple'}, {'price': '100'}")
    result = firebase.post('/products', "{'id': '3'}, {'name': 'apple'}, {'price': '150'}")
    result = firebase.get('/', None)

    return render(request,'webtestapp/index.html',my_dict)


