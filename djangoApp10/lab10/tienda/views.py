from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Producto
from .serializers import ProductoSerializer
# Create your views here.
 
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def producto_list(request):
        """
        List all code serie, or create a new serie.
        """
        if request.method == 'GET':
            productos = Producto.objects.all()
            serializer = ProductoSerializer(productos, many=True)
            return JSONResponse(serializer.data)
    
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    

