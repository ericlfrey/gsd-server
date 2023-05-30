"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Task, Project, Material


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

        task = Task.objects.get(pk=pk)
        serialized = SingleTaskSerializer(task)
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

    def update(self, request, pk=None):
        """Handle PUT requests for tasks"""
        task = Task.objects.get(pk=pk)
        name = request.data['name']
        details = request.data['details']
        due_date = request.data['due_date']
        task_status = request.data['status']
        task.name = name
        task.details = details
        task.due_date = due_date
        task.status = task_status
        task.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles Delete requests"""
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MaterialsTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'name',
            'price',
            'quantity',
            'acquired'
        )


class SingleTaskSerializer(serializers.ModelSerializer):
    """JSON serializer for single task"""
    materials = MaterialsTaskSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'project',
            'name',
            'details',
            'date_created',
            'due_date',
            'status',
            'materials'
        )
        depth = 1


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
            'status',
            'materials'
        )
        depth = 1
