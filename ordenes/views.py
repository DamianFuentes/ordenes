from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from PIL import Image
from .models import OrdenPapel
from .models import OrdenSistema
from django.contrib.auth.models import User
from .serializers import OrdenPapelSerializer
from .serializers import OrdenSistemaSerializer

@csrf_exempt
@api_view(['GET','POST'])
def ordenes_papel_list(request):
    """
    Lista de Ordenes y crear nueva orden
    """
    if request.method == 'GET':
        ordenes = OrdenPapel.objects.all()
        print(ordenes)
        serializer = OrdenPapelSerializer(ordenes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        print(request.data)
        serializer = OrdenPapelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET'])
def orden_papel_detail(request, entry):
    """
    Ver una Orden papel
    """
    try:
        orden = OrdenPapel.objects.filter(entrada=entry).last()
    except OrdenPapel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrdenPapelSerializer(orden)
        return JsonResponse(serializer.data,)
        

@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny, ))
def orden_papel_foto(request, entry):
    """
    Ver foto orden papel
    """

    if request.method == 'GET':
        try:
            orden = OrdenPapel.objects.filter(entrada=entry).last()
            return HttpResponse(orden.orden.read(), content_type="image/jpeg")
        except Exception as e :
            image_data = open("imgs_ordenes/not_found.jpg", "rb").read()
            return HttpResponse(image_data, content_type="image/jpeg")


@csrf_exempt
@api_view(['GET','POST'])
def ordenes_sistema_list(request):
    """
    Lista de Ordenes y crear nueva orden Orbital
    """
    if request.method == 'GET':
        ordenes = OrdenSistema.objects.all()
        print(ordenes)
        serializer = OrdenSistemaSerializer(ordenes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        print(request.data)
        serializer = OrdenSistemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET'])
def orden_sistema_detail(request, entry):
    """
    Ver una Orden Orbital
    """
    try:
        orden = OrdenSistema.objects.filter(entrada=entry).last()
    except OrdenSistema.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrdenSistemaSerializer(orden)
        return JsonResponse(serializer.data,)

@csrf_exempt
@api_view(['GET'])
def chequeo_credenciales(request):
    """
    Chequeo que sea usuario valido
    """
    if request.method == 'GET':
        return HttpResponse('Todo OK')