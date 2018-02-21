from rest_framework import serializers
from .models import ExpDB
## serialize take take the model and convert it to JSON


class ExpDBSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ExpDB  ## whic model to serialize
        #fields = ('project', 'gene', 'sample', 'fpkm');
        fields = '__all__' ## send back all the fields
    
