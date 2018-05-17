import csv
import random
from collections import OrderedDict

from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from cpdb_args.models import AntibioticClass, ARGene, InputFile, ARGPrimerPair, INPUT_FILE_HEADER
from cpdb_args.forms import InputFileForm


from cpdb.settings import INPUT_FILE_PASSWORD
# Create your views here.


class ARGHomeView(TemplateView):
    template_name = "cpdb_args/args_home.html"

    def get(self, request, *args, **kwargs):
        args_classes = AntibioticClass.objects.all().order_by('name')
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
            try:
                res = new_record.load_file()
                if res:
                    return redirect("/args/args_file_upload/{0}/".format(new_record.id))

            except Exception as e:
                new_record.delete()
                InputFile.restore_last_correct_file(InputFile)
                return render(request, self.template_name, {
                    'form': form,
                    'context': context,
                    'error': str(e)})

        else:
            return render(
                request, self.template_name, {
                    'form': form,
                    'context': context,
                    'error': "INVALID FORM DATA!"
                    })


class InputFileConfirmView(TemplateView):

    def _get_line_to_check(self, inputfile_id):
        line_to_check = random.choice(ARGPrimerPair.objects.all())
        sorted_values_list = []
        for key in INPUT_FILE_HEADER:
            if key == 'gene_name_variants':
                sorted_values_list.append(line_to_check.gene_name.name)
            elif key == 'antibiotic_class':
                sorted_values_list.append(line_to_check.antibiotic_class.name)
            else:
                sorted_values_list.append(line_to_check.__dict__[key])
        res = OrderedDict(zip(INPUT_FILE_HEADER, sorted_values_list))
        res['line_id'] = line_to_check.file_line_id
        res.move_to_end('line_id', last=False)

        return res

    def get(self, request, inputfile_id, *args, **kwargs):
        inputfile_instance = InputFile.objects.get(id=inputfile_id)
        if inputfile_instance.times_checked < 3:
            return render(request, "cpdb_args/args_input_check.html", {
                'line_to_check': self._get_line_to_check(inputfile_id),
                'inputfile_id': inputfile_id,
                'check_no': inputfile_instance.times_checked + 1
                })
        else:
            return render(request, "cpdb_args/args_input_success.html")

    def post(self, request, inputfile_id, *args, **kwargs):
        if request.POST["file_upload_password"] != INPUT_FILE_PASSWORD:
            return render(request, "cpdb_args/args_input_check.html", {
                'line_to_check': self._get_line_to_check(inputfile_id),
                'inputfile_id': inputfile_id,
                'error': "WRONG PASSWORD!",
                })

        elif request.POST['submit_value'] == 'incorrect':
            InputFile.objects.get(id=inputfile_id).delete()
            InputFile.restore_last_correct_file(InputFile)
            return redirect("cpdb_args:args_file_upload")

        else:
            inputfile_instance = InputFile.objects.get(id=inputfile_id)
            inputfile_instance.times_checked += 1
            inputfile_instance.save()

            if inputfile_instance.times_checked < 3:
                return render(request, "cpdb_args/args_input_check.html", {
                    'line_to_check': self._get_line_to_check(inputfile_id),
                    'inputfile_id': inputfile_id,
                    'check_no': inputfile_instance.times_checked + 1
                    })
            else:
                return render(request, "cpdb_args/args_input_success.html")
