from django.db import models

# Create your models here.

class Home(models.Model):
    home_text = models.TextField()
    header_title = models.CharField(max_length=120)
    header_subtitle = models.CharField(max_length=300)
    header_citation = models.CharField(max_length=200)
    to_notify_email = models.EmailField(verbose_name="Your email")


class Contact(models.Model):
    address = models.TextField()
    email_contact = models.EmailField()
    group_website = models.URLField(max_length=200)


class AntibioticClass(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class TargetGene(models.Model):
    name = models.CharField(max_length=100)
    antibiotic_class = models.ForeignKey(AntibioticClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + self.antibiotic_class.name + ')'  


class PrimerPair(models.Model):
    name = models.CharField(max_length=50)
    primer_for_seq = models.CharField(max_length=100)
    primer_rev_seq = models.CharField(max_length=100)
    target_gene = models.ForeignKey(TargetGene, on_delete=models.CASCADE)


class FileLink(models.Model):
    name = models.CharField(max_length=200)
    file_url = models.URLField(max_length=200)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name