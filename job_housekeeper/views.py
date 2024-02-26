import json
from django.shortcuts import render
from.models import *
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework import generics
# Create your views here.

@permission_classes([AllowAny])
class JobrequestCreateView(generics.CreateAPIView):
    queryset = Jobrequest.objects.all()
    serializer_class = JobrequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@permission_classes([AllowAny])
class JobrequestUpdateView(generics.UpdateAPIView):
    queryset = Jobrequest.objects.all()
    serializer_class = JobrequestSerializerUpdate

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@permission_classes([AllowAny])
class JobrequestListView(generics.ListAPIView):
    queryset = Jobrequest.objects.all()
    serializer_class = JobrequestSerializer

@permission_classes([AllowAny])
class JobrequestRetrieveView(generics.RetrieveAPIView):
    queryset = Jobrequest.objects.all()
    serializer_class = JobrequestSerializer

@permission_classes([AllowAny])
class GetJpobStatusListView(generics.ListAPIView):
    queryset = Jobstatus.objects.all()
    serializer_class = JobstatusSerializer

@permission_classes([AllowAny])
class GetPlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

@permission_classes([AllowAny])
class RsponsiblePersonListView(generics.ListAPIView):
    queryset = RsponsiblePerson.objects.all()
    serializer_class = RsponsiblePersonSerializer