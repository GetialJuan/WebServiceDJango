from rest_framework import viewsets
from productos.models import Producto
from .serializers import ProductoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoApiView(APIView):
    
    def get(self, request, format=None):
        productos = Producto.objects.all()
        producto_serializer = ProductoSerializer(productos, many=True)
        return Response(producto_serializer.data)