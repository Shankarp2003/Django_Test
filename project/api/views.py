from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ProjectCreateSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs['pk'])
        serializer.save(client=client, created_by=self.request.user)

class AssignedProjectsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve projects assigned to the current user
        projects = Project.objects.filter(users=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
