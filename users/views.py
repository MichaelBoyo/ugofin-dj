from django.shortcuts import render, HttpResponse
from pymongo import MongoClient


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")
