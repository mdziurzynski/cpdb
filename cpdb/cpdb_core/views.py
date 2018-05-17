from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from cpdb_core.models import Home, Contact

class HomeView(TemplateView):
    template_name = "cpdb_core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ContactView(TemplateView):
    template_name = "cpdb_core/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['object'] = Contact.objects.first()
        print(context)
        return context
