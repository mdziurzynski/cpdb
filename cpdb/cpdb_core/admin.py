from django.contrib import admin

from .models import AntibioticClass, Contact, Home, TargetGene

# Register your models here.
admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(TargetGene)

class TargetGeneInline(admin.TabularInline):
    model = TargetGene

class AntibioticClassAdmin(admin.ModelAdmin):
    inlines = [
        TargetGeneInline,
    ]

admin.site.register(AntibioticClass, AntibioticClassAdmin)
