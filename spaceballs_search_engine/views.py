from django.shortcuts import render

from .forms import SearchForm
from .models import Quote

def homepage(request):
    form = SearchForm(request.POST)
    context = {'form': form}

    # If form was submitted
    if request.method == 'POST':
        if form.is_valid():
            character = form.cleaned_data['character']
            line = form.cleaned_data['line']

            if line and character:
                context['quotes'] = Quote.objects.filter(character__iexact=character, line__icontains=line)

            if line:
                context['quotes'] = Quote.objects.filter(line__icontains=line)

            if character:
                context['quotes'] = Quote.objects.filter(character__iexact=character)


    return render(request, 'spaceballs_search_engine/homepage.html', context)