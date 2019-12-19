from django.shortcuts import render, redirect
from .models import quotes
import random
import json
from django.core import serializers

def show(request):
    json_serializer = serializers.get_serializer("json")()
    Quotes = json_serializer.serialize(quotes.objects.all(), ensure_ascii=False)
    number = quotes.objects.count()
    context = {'number' : number,
               'Quotes' : Quotes}
    
    return render(request, 'bootQuotes.html', context) 



def all(request):
    Quotes = quotes.objects.all()
    context = {'quotes' : Quotes}
    return render(request, 'allPage.html', context)

def rand(request):
    Quote = quotes.objects.all() 
    context = {'quote' : Quote }
    return render(request, 'randPage.html', context)
