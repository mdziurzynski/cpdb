from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from cpdb_core.models import Home, Contact, AntibioticClass


# Create your views here.
class HomeView(TemplateView):
    template_name = "cpdb_core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context


class ContactView(TemplateView):
    template_name = "cpdb_core/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

class ARClassListView(ListView):

    model = AntibioticClass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = AntibioticClass.objects.all().order_by('name')
        print(context)
        return context

class ARClassDetailView(DetailView):

    model = AntibioticClass

    def get_context_data(self, **kwargs):
        context = super(ARClassDetailView, self).get_context_data(**kwargs)
        return context
