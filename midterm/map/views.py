from django.shortcuts import render
from django.views.generic import ListView, DetailView
from map.models import Map
from django.views.generic import FormView
from map.forms import MapSearchForm
from django.db.models import Q
from django.shortcuts import render


class mapLV(ListView):
    model = Map
    template_name = 'map/map_all.html'
    context_object_name = 'maps'
    paginate_by = 5

class mapDV(DetailView):
    model = Map



class SearchFormView(FormView):
    form_class = MapSearchForm
    template_name = 'map/map_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        maps_list = Map.objects.filter(
            Q(title__icontains=searchWord) | Q(country__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = maps_list

        return render(self.request, self.template_name, context)