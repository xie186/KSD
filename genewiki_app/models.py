from django.db import models
from django.utils.text import slugify
from django.contrib import admin

# Create your models here.
class Gene(models.Model):
    geneid = models.CharField(max_length=256, primary_key=True)
    coordinate = models.CharField(max_length=256)
    strand = models.CharField(max_length=1)
    best_ara = models.CharField(max_length=1000)
    function_des = models.CharField(max_length=1000)

    def __str__(self):
        return self.geneid

class GO(models.Model):
    ## gene1   GO:00012        BP      Sugur
    accession = models.CharField(max_length=256)
    namespace = models.CharField(max_length=256) 
    description = models.CharField(max_length=256)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE) 
    def __str__(self):
        return "%s %s" % (self.accession, self.gene.geneid)
    
    class Meta:
        verbose_name = "GO"
        verbose_name_plural = "GO"

class Project(models.Model):
    title = models.CharField(max_length=256, primary_key=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField(null=True)
    def __str__(self):
        return self.title

#class ProjectAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("name",)}


class ExpDB(models.Model):
    #project 1       gene1   leaf    200
    project = models.CharField(max_length=256)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    sample = models.CharField(max_length=256)
    fpkm = models.FloatField()
    def __str__(self):
        return "%s : %s : %s" % (self.project, self.gene, self.sample)
    class Meta:
        verbose_name = "ExpDB"
        verbose_name_plural = "ExpDB"
 
