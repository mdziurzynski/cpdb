from django.forms import ModelForm
from cpdb_args.models import InputFile


class InputFileForm(ModelForm):
    class Meta:
        model = InputFile
        fields = ['uploaded_file']
