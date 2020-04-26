from django.shortcuts import render

from django.http import HttpResponse

from .models import Quote

def homepage(request):
    test_quote = Quote.objects.get(pk=1)
    return HttpResponse(test_quote)