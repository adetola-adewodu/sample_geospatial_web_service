
from rest_framework import viewsets

from locations.models import Location, State, Nhdarea
from locations.serializers import LocationSerializer, StateSerializer,NhdareaSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def location_list(request):
    """
    List all locations, or create a new location.
    """
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def state_list(request):
    """
    List all locations, or create a new location.
    """
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def nhdarea_list(request):
    """
    List all locations, or create a new location.
    """
    if request.method == 'GET':
        nhdarea = Nhdarea.objects.all()
        serializer = NhdareaSerializer(nhdarea, many=True)
        return JSONResponse(serializer.data)