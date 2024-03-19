from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from iron.models import User
from iron.serializers.user_serializer import users_serializer
import json
import traceback

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
                subject = params['subject'],
                description = params['description'],
                projects = _map_checkbox_projects(params['checkboxProjects']),
                professions = _map_checkbox_professions(params['checkboxProfessions']),
                hear_about_us = 'Other' if params['hearAboutUs'] == 'Choose an option' else params['hearAboutUs']
            )

            return JsonResponse({'message': 'Record created successfully'}, status=200)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'method not allowed'}, status=405)

def _map_checkbox_projects(checkbox_projects):
    dictionary_projects = {
        'balconies': 'Balconies',
        'doors': 'Doors',
        'fences': 'Fences',
        'furniture': 'Furniture',
        'gates': 'Gates',
        'homeDecor': 'Home Decor',
        'lighting': 'Lighting',
        'railings': 'Railings',
        'restoration': 'Restoration',
        'sculptures': 'Sculptures',
        'wineCellars': 'Wine Cellars',
        'other': 'Other'
    }

    mapped_projects = []

    for key in checkbox_projects.keys():
        if key in dictionary_projects:
            mapped_projects.append(dictionary_projects[key])

    return mapped_projects

def _map_checkbox_professions(checkbox_professions):
    dictionary_professions = {
      'homeOwner': 'Home Owner',
      'designer': 'Designer',
      'architect': 'Architect',
      'contractor': 'Contractor',
      'other': 'Other'
    }

    mapped_professions = []

    for key in checkbox_professions.keys():
        if key in dictionary_professions:
            mapped_professions.append(dictionary_professions[key])

    return mapped_professions