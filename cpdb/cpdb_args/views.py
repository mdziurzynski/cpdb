import csv

from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from cpdb_args.models import AntibioticClass, ARGene, INPUT_FILE_HEADER
from cpdb_args.forms import InputFileForm


from cpdb.settings import INPUT_FILE_PASSWORD
# Create your views here.


class ARGHomeView(TemplateView):
    template_name = "cpdb_args/args_home.html"

    def get(self, request, *args, **kwargs):
        args_classes = AntibioticClass.objects.all()
        return render(request, self.template_name, {'object_list': args_classes})


class AntibioticClassView(TemplateView):
    template_name = "cpdb_args/antibiotic_class.html"

    def get(self, request, antibiotic_class_id, *args, **kwargs):
        argenes = AntibioticClass.objects.get(pk=antibiotic_class_id).argene_set.all()
        return render(request, self.template_name, {'object_list': argenes})


class ARGeneView(TemplateView):
    template_name = "cpdb_args/argene_details.html"

    def get(self, request, argene_id, *args, **kwargs):
        argenes = ARGene.objects.get(pk=argene_id).argprimerpair_set.all()
        return render(request, self.template_name, {'object_list': argenes})


class InputFileView(TemplateView):
    template_name = "cpdb_args/args_input_file_1.html"
    form_class = InputFileForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        return render(request, self.template_name, {'form': form, 'context': context})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)
        context = super().get_context_data(**kwargs)

        if request.POST.get("file_upload_password", False) != INPUT_FILE_PASSWORD:
            return render(request, self.template_name, {'form': form, 'context': context, 'error': "WRONG PASSWORD!"})

        if form.is_valid():

            print("success")

            new_record = form.save()
            with open(new_record.uploaded_file.path) as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                if header != INPUT_FILE_HEADER:
                    new_record.delete()
                    return render(request, self.template_name, {
                        'form': form,
                        'context': context,
                        'error': "BAD CSV HEADER!<br/><br/>RECEIVED HEADER:{0}".format(header)})
            new_record.clone_tables()
            
        else:
            return render(request, self.template_name, {'form': form, 'context': context, 'error': "INVALID FORM DATA!"})


# class ARClassListView(ListView):

#     model = AntibioticClass

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_list'] = AntibioticClass.objects.all().order_by('name')
#         print(context)
#         return context

# class ARClassDetailView(DetailView):

#     model = AntibioticClass

#     def get_context_data(self, **kwargs):
#         context = super(ARClassDetailView, self).get_context_data(**kwargs)
#         return context


# class TargetGeneDetailView(DetailView):

#     model = TargetGene

#     def get_context_data(self, **kwargs):
#         context = super(TargetGeneDetailView, self).get_context_data(**kwargs)
#         return context


# class FileLinkListView(ListView):

#     model = FileLink

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object_list'] = FileLink.objects.all().order_by('creation_datetime')
#         print(context)
#         return context