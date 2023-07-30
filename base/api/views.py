from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
#javascript object notetion(Json), it is a format of data

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    # we need to convert python objects into ig json type for which we will use serializer
    seializer = RoomSerializer(rooms, many=True)
    return Response(seializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room=Room.objects.get(id=pk)
    seializer = RoomSerializer(room, many=False)
    return Response(seializer.data)