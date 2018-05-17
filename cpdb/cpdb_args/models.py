from django.db import models
import csv
import re

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

INPUT_FILE_COLS_TYPES = [
    str, str, str, str, str, str, float, float, str, float, float, float, float,
    float, float, float, float, float, float, float, float, float, float,
    float, '%', float, float, '%', float, float, str, str, float, '%', float,
    float, float]


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

    file_line_id = models.IntegerField()

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
    elongation_time = models.CharField(max_length=10)
    annealing_temp = models.FloatField()
    reference_sequence_coverage = models.FloatField()
    min_refseq_lenght = models.FloatField()
    max_refseq_lenght = models.FloatField()
    difference_refseq_lenght = models.FloatField()

class InputFile(models.Model):

    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_file = models.FileField()

    def load_file(self):

        # 1. build dicts with cleaned data
        unique_anti_class = {}
        unique_gene = {}
        res_lines = []
        with self.uploaded_file.open("rt") as input_file:
            reader = csv.reader(csvfile)

            # skipping header
            _ = next(reader)

            for line in reader:
                cleaned_line = []
                line_with_types = zip(line, INPUT_FILE_COLS_TYPES)
                for pair in line_with_types:
                    if pair[1] == str:
                        cleaned_line.push(pair[0])
                    elif pair[1] == float:
                        cleaned_line.push(float(pair[0]))
                    elif pair[1] == '%':
                        data = float(pair[0].strip('%')) / 100
                        cleaned_line.append(data)

                line_dict = dict(zip(INPUT_FILE_HEADER, cleaned_line))

                line_dict['antibiotic_class'] = line_dict['antibiotic_class'].capitalize()
                line_dict["gene_name"] = re.sub('_[1-9]*$', '', line_dict["gene_name_variants"])
                del line_dict['gene_name_variants']

                unique_anti_class[line_dict['antibiotic_class']] = 0
                unique_gene[line_dict["gene_name_variants"]] = 0
                res_lines.append(line_dict)

        # 2. delete data in anti_class, gene and primer pair tables
        AntibioticClass.objects.all().delete()
        ARGene.objects.all().delete()
        ARGPrimerPair.objects.all().delete()

        # 3. Iterate through build dict and input data
        for anti_class_name in unique_anti_class:
            new = AntibioticClass.objects.create(name=anti_class_name)
            new.save()
            unique_anti_class[anti_class_name] = new.id

        for gene_name in unique_gene:
            new = ARGene.objects.create(name=gene_name)
            new.save()
            unique_gene[gene_name] = new.id



    def restore_last_correct_file(self):
        last_correct_instance = self.objects.last()
        last_correct_instance.load_file()
        return True

# class FileLink(models.Model):
#     name = models.CharField(max_length=200)
#     file_url = models.URLField(max_length=200)
#     creation_datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name