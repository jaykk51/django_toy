from django.shortcuts import render
from django.views.generic import ListView, DetailView
from club.models import Club
from django.views.generic import FormView
from club.forms import ClubSearchForm
from django.db.models import Q
from django.shortcuts import render

class clubLV(ListView):
    model = Club
    template_name = 'club/club_all.html'
    context_object_name = 'clubs'
    paginate_by = 5

class clubDV(DetailView):
    model = Club

class SearchFormView(FormView):
    form_class = ClubSearchForm
    template_name = 'club/club_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        clubs_list = Club.objects.filter(Q(name__icontains=searchWord) |
                                         Q(city__icontains=searchWord) |
                                         Q(content__icontains=searchWord) |
                                         Q(location__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = clubs_list

        return render(self.request, self.template_name, context)
