from haystack import indexes 
from .models import Gene, GO 

class GeneIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    geneid = indexes.CharField(model_attr='geneid')
    best_ara = indexes.CharField(model_attr='best_ara')
    function_des = indexes.CharField(model_attr='function_des')
    def get_model(self):
        #print(Gene)
        return Gene
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class GOIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    accession = indexes.CharField(model_attr='accession')
    description = indexes.CharField(model_attr='description') 

    def get_model(self):
        return GO
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
