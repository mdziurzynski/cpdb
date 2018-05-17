from django.contrib import admin

# Register your models here.
from cpdb_args.models import AntibioticClass, ARGene

admin.site.register(AntibioticClass)
admin.site.register(ARGene)

# admin.site.register(Home)
# admin.site.register(Contact)
# admin.site.register(TargetGene)

# class TargetGeneInline(admin.TabularInline):
#     model = TargetGene

# class AntibioticClassAdmin(admin.ModelAdmin):
#     inlines = [
#         TargetGeneInline,
#     ]

# admin.site.register(AntibioticClass, AntibioticClassAdmin)
# admin.site.register(PrimerPair)
# admin.site.register(FileLink)