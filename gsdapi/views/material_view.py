"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Material, Project, Task


class MaterialView(ViewSet):
    """GSD API materials view"""

    def list(self, request):
        """Handle GET requests to get all materials

        Returns:
            Response -- JSON serialized list of materials
        """

        materials = Material.objects.all()
        serialized = MaterialSerializer(materials, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single materials

        Returns:
            Response -- JSON serialized materials record
        """

        materials = Material.objects.get(pk=pk)
        serialized = MaterialSerializer(materials)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests for materials

        Returns:
            Response: JSON serialized representation of newly created material
        """
        new_material = Material()
        if 'task' in request.data:
            new_material.task = Task.objects.get(id=request.data['task'])
        new_material.project = Project.objects.get(id=request.data['project'])
        new_material.name = request.data['name']
        new_material.price = request.data['price']
        new_material.quantity = request.data['quantity']
        new_material.acquired = request.data['acquired']
        new_material.save()

        serialized = MaterialSerializer(new_material)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for materials"""
        material = Material.objects.get(pk=pk)

        if 'task' in request.data:
            if request.data['task'] is not None:
                task = Task.objects.get(id=request.data['task'])
                material.task = task
        name = request.data['name']
        price = request.data['price']
        quantity = request.data['quantity']
        acquired = request.data['acquired']

        material.name = name
        material.price = price
        material.quantity = quantity
        material.acquired = acquired

        material.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles Delete requests"""
        material = Material.objects.get(pk=pk)
        material.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MaterialSerializer(serializers.ModelSerializer):
    """JSON serializer for materials"""
    class Meta:
        model = Material
        fields = (
            'id',
            'project',
            'task',
            'name',
            'price',
            'quantity',
            'acquired'
        )
        depth = 1
