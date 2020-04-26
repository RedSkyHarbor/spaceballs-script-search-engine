from django.shortcuts import render

from .models import Quote

def homepage(request):
    all_quotes = Quote.objects.all()
    context = {'all_quotes': all_quotes}
    return render(request, 'spaceballs_search_engine/homepage.html', context)