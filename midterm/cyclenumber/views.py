from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cyclenumber.models import Cyclenumber
from django.views.generic import FormView
from cyclenumber.forms import CyclenumberSearchForm
from django.db.models import Q
from django.shortcuts import render



class cyclenumberLV(ListView):
    model = Cyclenumber
    template_name = 'cyclenumber/cyclenumber_all.html'
    context_object_name = 'cyclenumbers'
    paginate_by = 5

class cyclenumberDV(DetailView):
    model = Cyclenumber


class SearchFormView(FormView):
    form_class = CyclenumberSearchForm
    template_name = 'cyclenumber/cyclenumber_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        cyclenumbers_list = Cyclenumber.objects.filter(
            Q(name__icontains=searchWord) | Q(modelname__icontains=searchWord)
            | Q(brand__icontains=searchWord) | Q(number__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = cyclenumbers_list

        return render(self.request, self.template_name, context)