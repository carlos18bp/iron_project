from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from iron.models import User
from iron.serializers.user_serializer import users_serializer
import json

def index(request):
    """
    Index view to return a JSON users serialized reponse.

    :param request: Django object request.
    :type request: django.http.HttpRequest

    :return: JSON users serialized reponse.
    :rtype: django.http.JsonResponse
    """
    users = User.objects.all().order_by('-id')
    
    return JsonResponse(users_serializer(users), safe=False)

def create(request):
    """
    Create view to return a JSON users serialized and status reponse.

    :param request: Django object request.
    :type request: django.http.HttpRequest

    :return: JSON users serialized and status reponse.
    :rtype: django.http.JsonResponse
    """
    if request.method == 'POST':
        try:
            params = json.loads(request.body.decode('utf-8'))

            User.objects.create(
                first_name = params['firstName'],
                last_name = params['lastName'],
                email = params['email'],
                contact = params['contact'],
            )

            return JsonResponse({'message': 'Record created successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'method not allowed'}, status=405)