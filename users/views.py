from django.shortcuts import render, HttpResponse
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jake:dQljZgVzeOnVsMZE@merndb.uls2ewf.mongodb.net/ugofinance?retryWrites=true&w=majority')
db = client['ugofinance']

def index(request):
    return HttpResponse("Hello, world. You're at the users index.")
