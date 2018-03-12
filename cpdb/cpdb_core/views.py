from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from cpdb_core.models import Home, Contact, AntibioticClass, TargetGene, FileLink
from cpdb_core.forms import HomeForm

class HomeView(TemplateView):
    template_name = "cpdb_core/home.html"
    form_class = HomeForm


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as error:
                error_message = str(error)
                return render(request, self.template_name, {'form': form, 'error': error_message})

            return HttpResponseRedirect('/notification_email_success/')

        return render(request, self.template_name, {'form': form})


# # Create your views here.
# class HomeView(TemplateView):
#     template_name = "cpdb_core/home.html"

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['email_field'] = 
#         #context['latest_articles'] = Article.objects.all()[:5]
#         return context


class ContactView(TemplateView):
    template_name = "cpdb_core/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['object'] = Contact.objects.first()
        print(context)
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


class TargetGeneDetailView(DetailView):

    model = TargetGene

    def get_context_data(self, **kwargs):
        context = super(TargetGeneDetailView, self).get_context_data(**kwargs)
        return context


class FileLinkListView(ListView):

    model = FileLink

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = FileLink.objects.all().order_by('creation_datetime')
        print(context)
        return context

# class PrimerPairDetailView(DetailView):

#     model = PrimerPair

#     def get_context_data(self, **kwargs):
#         context = super(PrimerPairDetailView, self).get_context_data(**kwargs)
#         return context
