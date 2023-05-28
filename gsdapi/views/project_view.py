"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Project


class ProjectView(ViewSet):
    """GSD API Projects view"""

    def list(self, request):
        """Handle GET requests to get all projects

        Returns:
            Response -- JSON serialized list of Projects
        """

        projects = Project.objects.all()
        serialized = ProjectSerializer(projects, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single projects

        Returns:
            Response -- JSON serialized projects record
        """

        projects = Project.objects.get(pk=pk)
        serialized = ProjectSerializer(projects)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests for projects

        Returns:
            Response: JSON serialized representation of newly created project
        """
        new_project = Project()
        new_project.user = request.auth.user
        new_project.title = request.data['title']
        new_project.date_created = request.data['date_created']
        new_project.save()

        serialized = ProjectSerializer(new_project)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for projects"""
        project = Project.objects.get(pk=pk)
        title = request.data['title']
        project.title = title
        project.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles Delete requests"""
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProjectSerializer(serializers.ModelSerializer):
    """JSON serializer for projects"""
    class Meta:
        model = Project
        fields = (
            'id',
            'user',
            'title',
            'date_created',
            'tasks',
            'materials'
        )
        depth = 2
