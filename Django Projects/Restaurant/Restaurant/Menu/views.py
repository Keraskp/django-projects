from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializers import *
from .models import *

class GetMenu(APIView):
    def get(self, request):
        menu = Menu.objects.all()
        serializer = MenuSerializers(menu, many=True)
        return Response(serializer.data)

class AddItem(APIView):
    def post(self, request):
        serializer = MenuSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'message' : 'Item added to Menu'})