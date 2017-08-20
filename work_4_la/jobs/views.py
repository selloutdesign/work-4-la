# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import JobSerializer

from .models import Job
from .filters import JobFilter

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.

class AuthListView(generics.ListCreateAPIView):
   
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_fields = ('occupational_category', 'categories')
    permission_classes = (IsAuthenticated,)
     
    def perform_create(self, serializer):
        serializer.save()

class CreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_fields = ('occupational_category', 'categories')
    
    def perform_create(self, serializer):
        serializer.save()
        
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class DetailView(generic.DetailView):
    model = Job
    template_name = 'detail.html'

def jobsearch(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job_list.html', {'filter': job_filter})