from firebase import firebase
#firebase = firebase.FirebaseApplication('https://rezo-sandbox.firebaseio.com', None)
firebase = firebase.FirebaseApplication('https://rezo-sandbox.firebaseio.com', None)
result = firebase.post('/products', "{'id': '1'}, {'name': 'orange'}, {'price': '50'}")
result = firebase.post('/products', "{'id': '2'}, {'name': 'apple'}, {'price': '100'}")
result = firebase.post('/products', "{'id': '3'}, {'name': 'apple'}, {'price': '150'}")
result = firebase.get('/', None)
print(result)