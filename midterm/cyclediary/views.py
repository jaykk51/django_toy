from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView
from cyclediary.models import Cyclediary
from django.views.generic import FormView
from cyclediary.forms import CyclediarySearchForm
from django.db.models import Q
from django.shortcuts import render

class CyclediaryLV(ListView):
    model = Cyclediary
    template_name = 'cyclediary/cyclediary_all.html'
    context_object_name = 'diaries'
    paginate_by = 5


class CyclediaryDV(DetailView):
    model = Cyclediary


class CyclediaryAV(ArchiveIndexView):
    model = Cyclediary
    date_field = 'diary_dt'


class CyclediaryYAV(YearArchiveView):
    model = Cyclediary
    date_field = 'diary_dt'
    make_object_list = True


class CyclediaryMAV(MonthArchiveView):
    model = Cyclediary
    date_field = 'diary_dt'



class CyclediaryDAV(DayArchiveView):
    model = Cyclediary
    date_field = 'diary_dt'


class CyclediaryTAV(TodayArchiveView):
    model = Cyclediary
    date_field = 'diary_dt'



class SearchFormView(FormView):
    form_class = CyclediarySearchForm
    template_name = 'cyclediary/cyclediary_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        diary_list = Cyclediary.objects.filter(Q(title__icontains=searchWord)
                                               | Q(description__icontains=searchWord)
                                               | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = diary_list

        return render(self.request, self.template_name, context)

