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


class ProjectSerializer(serializers.ModelSerializer):
    """JSON serializer for projects"""
    class Meta:
        model = Project
        fields = (
            'id',
            'user',
            'title',
            'date_created'
        )
        depth = 1
