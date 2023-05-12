"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gsdapi.models import Material


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
