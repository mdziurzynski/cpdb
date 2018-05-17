from django.db import models

# Create your models here.
INPUT_FILE_HEADER = [
    'antibiotic_class', 'gene_name_variants', 'fwd', 'fwd_seq', 'rev',
    'rev_seq', 'product_length', 'product_length_deviation', 'ref_db',
    'min_qcovhsp', 'min_pident', 'specificity', 'efficacy', 'taxonomy_efficacy',
    'correct_products_number', 'products_number', 'correct_products_vs_unique_refs',
    'unique_ref_seqs_number', 'ref_seqs_number', 'taxons_in_products',
    'taxons_in_refs', 'extra_different_taxons_amongst_products', 'extra_products',
    'primerf_lenght', 'primerf_gccontent', 'primerf_mt', 'primerr_lenght',
    'primerr_gccontent', 'primerr_mt', 'primer_pair_tm_difference', 'qpcr_usage',
    'elongation_time', 'annealing_temp', 'reference_sequence_coverage',
    'min_refseq_lenght', 'max_refseq_lenght', 'difference_refseq_lenght']


class AntibioticClass(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ARGene(models.Model):
    name = models.CharField(max_length=100)
    antibiotic_class = models.ForeignKey(AntibioticClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + self.antibiotic_class.name + ')'  


class ARGPrimerPair(models.Model):
    name = models.CharField(max_length=50)
    primer_for_seq = models.CharField(max_length=100)
    primer_rev_seq = models.CharField(max_length=100)

    # input table columns
    antibiotic_class = models.ForeignKey(AntibioticClass)
    gene_name = models.ForeignKey(ARGene)

    fwd = models.CharField(max_length=100)
    fwd_seq = models.CharField(max_length=100)
    rev = models.CharField(max_length=100)
    rev_seq = models.CharField(max_length=100)
    product_length = models.FloatField()
    product_length_deviation = models.FloatField()
    ref_db = models.CharField(max_length=100)
    min_qcovhsp = models.FloatField()
    min_pident = models.FloatField()
    specificity = models.FloatField()
    efficacy = models.FloatField()
    taxonomy_efficacy = models.FloatField()
    correct_products_number = models.FloatField()
    products_number = models.FloatField()
    correct_products_vs_unique_refs = models.FloatField()
    unique_ref_seqs_number = models.FloatField()
    ref_seqs_number = models.FloatField()
    taxons_in_products = models.FloatField()
    taxons_in_refs = models.FloatField()
    extra_different_taxons_amongst_products = models.FloatField()
    extra_products = models.FloatField()
    primerf_lenght = models.FloatField()
    primerf_gccontent = models.FloatField()
    primerf_mt = models.FloatField()
    primerr_lenght = models.FloatField()
    primerr_gccontent = models.FloatField()
    primerr_mt = models.FloatField()
    primer_pair_tm_difference = models.FloatField()
    qpcr_usage = models.CharField(max_length=100)
    elongation_time = models.FloatField()
    annealing_temp = models.FloatField()
    reference_sequence_coverage = models.FloatField()
    min_refseq_lenght = models.FloatField()
    max_refseq_lenght = models.FloatField()
    difference_refseq_lenght = models.FloatField()

class InputFile(models.Model):

    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.FileField()


# class FileLink(models.Model):
#     name = models.CharField(max_length=200)
#     file_url = models.URLField(max_length=200)
#     creation_datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name