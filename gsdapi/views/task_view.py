"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Task


class TaskView(ViewSet):
    """GSD API tasks view"""

    def list(self, request):
        """Handle GET requests to get all tasks

        Returns:
            Response -- JSON serialized list of tasks
        """

        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single tasks

        Returns:
            Response -- JSON serialized tasks record
        """

        tasks = Task.objects.get(pk=pk)
        serialized = TaskSerializer(tasks)
        return Response(serialized.data, status=status.HTTP_200_OK)


class TaskSerializer(serializers.ModelSerializer):
    """JSON serializer for tasks"""
    class Meta:
        model = Task
        fields = (
            'id',
            'project',
            'name',
            'details',
            'date_created',
            'due_date',
            'status'
        )
        depth = 1
