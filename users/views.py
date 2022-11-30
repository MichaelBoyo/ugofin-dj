from django.shortcuts import render, HttpResponse
from pymongo import MongoClient


def index(request):
    return render(request, 'users/index.html')
