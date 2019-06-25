from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from PIL import Image
from .models import Orden
from .serializers import OrdenSerializer


@csrf_exempt
@api_view(['GET','POST'])
def ordenes_list(request):
    """
    Lista de Ordenes y crear nueva orden
    """
    if request.method == 'GET':
        ordenes = Orden.objects.all()
        print(ordenes)
        serializer = OrdenSerializer(ordenes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        print(request.data)
        serializer = OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET'])
def orden_detail(request, pk):
    """
    Ver una Orden.
    """
    try:
        orden = Orden.objects.get(pk=pk)
    except Orden.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrdenSerializer(orden)
        return JsonResponse(serializer.data,)


@api_view(['GET'])
def orden_foto(request, pk):
    """
    Ver una Orden.
    """
    try:
        orden = Orden.objects.get(pk=pk)
    except Orden.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return HttpResponse(orden.orden.read(), content_type="image/jpeg")
