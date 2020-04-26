from django.shortcuts import render

from .forms import SearchForm
from .models import Quote

def homepage(request):
    form = SearchForm(request.POST)
    all_quotes = Quote.objects.all()
    context = {'quotes': all_quotes, 'form': form}
    return render(request, 'spaceballs_search_engine/homepage.html', context)