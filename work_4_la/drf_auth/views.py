from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, permissions 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins


from .permissions import IsAuthenticatedOrCreate
from .serializers import SignUpSerializer, GroupSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User, Group
from work_4_la.users.models import User

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class GroupViewSet(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    def options(self, request, *args, **kwargs):
        # queryset = Group.objects.all()
        # serializer_class = GroupSerializer
        content = {'answer': 3}
        return Response( content, status=status.HTTP_200_OK)
        
    # def get(self, request, format=None):
    #     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    #     required_scopes = ['groups']
    #     queryset = Group.objects.all()
    #     serializer_class = GroupSerializer
    #     return Response(serializer_class.data)
    