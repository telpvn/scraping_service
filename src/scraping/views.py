from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    # print(request.POST)
    form = FindForm()
    city = request.GET.get('city')
    Language = request.GET.get('Language')
    qs = []
    if city or Language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if Language:
            _filter['Language__slug'] = Language

        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs,
                                                  'form': form})
