from django.db import models

# Create your models here.

class Home(models.Model):
    home_text = models.TextField()
    header_title = models.CharField(max_length=120)
    header_subtitle = models.CharField(max_length=300)
    header_citation = models.CharField(max_length=200)


class Contact(models.Model):
    address = models.TextField()
    email_contact = models.EmailField()
    group_website = models.URLField(max_length=200)
