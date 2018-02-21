from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import JsonResponse

##API###
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ExpDB, Project
from genewiki_app.serializers import ExpDBSerializer
#####

from genewiki_app import models
# Create your views here.

class GeneDetailView(DetailView):
    model = models.Gene
    
    def get_context_data(self, **kwargs):
        context = super(GeneDetailView, self).get_context_data(**kwargs)
        context['go_list'] = models.GO.objects.all().filter(gene = self.object)
        context['project_list'] = models.Project.objects.all().filter()
        
        #context['project'] = models.Project.objects.all().filter()
        ##print(context['go_list'])
        #context['now'] = timezone.now()
        return context

class ExpDBList(APIView):
 
    def get(self, request):
        expdb = ExpDB.objects.all()
        serializer = ExpDBSerializer(expdb, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class ExpDBListGene(generics.ListAPIView):
    serializer_class = ExpDBSerializer 
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        geneid = self.kwargs['geneid']
        print(self.kwargs)
        return ExpDB.objects.filter(gene=geneid)

class ExpDBGenePro(generics.ListAPIView):
    serializer_class = ExpDBSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        geneid = self.kwargs['geneid']
        pro_slug = self.kwargs['pro_slug']
        #print(self.kwargs) 
        project = list(Project.objects.filter(slug=pro_slug))[0]
        #print(pro_slug)
        print(project)
        return ExpDB.objects.filter(gene=geneid, project=project)

#def gene_expdb(request):
#    pro_gene = request.GET.get('pro_gene', None)
#    project_slug, gene_id = pro_gene.split('/')
#    print(projet_slug+"\txx\t"+gene_id)
#    gene_model = models.Gene.all().filter(geneid = gene_id)
#    project_model = models.Project.all().filter(slug=project_slug)
#    project_name = list(project_model)[0].title
#    data = models.ExpDB.objects.all().filter(project=project_name, gene=list(gene_model)[0])
#    return JsonResponse(data)
#
