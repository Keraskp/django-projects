from rest_framework.response import Response # Response Class for rendering response
from rest_framework.decorators import api_view # Decorator for bind REST Methods

# Define Request Handlers here

@api_view(['GET'])
def getData(request):
    person = {'name': 'Aditya Kiran', 'age': 21}
    return Response(person)  # dictionary will be output as JSON
