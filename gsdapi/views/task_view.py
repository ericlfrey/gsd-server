"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Task, Project


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

    def create(self, request):
        """Handle POST requests for tasks

        Returns:
            Response: JSON serialized representation of newly created task
        """
        new_task = Task()
        new_task.project = Project.objects.get(id=request.data['project'])
        new_task.name = request.data['name']
        new_task.details = request.data['details']
        new_task.date_created = request.data['date_created']
        new_task.due_date = request.data['due_date']
        new_task.status = request.data['status']
        new_task.save()

        serialized = TaskSerializer(new_task)

        return Response(serialized.data, status=status.HTTP_201_CREATED)


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
