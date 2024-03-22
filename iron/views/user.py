from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from iron.models import User
from iron.serializers.user_serializer import users_serializer
import json
import traceback
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


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
            email_sender()

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

def email_sender():
    # Renderiza el contenido HTML desde una plantilla
    html_content = render_to_string('NewMessage.html', {'message': 'HOLAAAAAAAAAA'})

    subject = "Oh Yeah Look At This A New Function for Sell"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['carlos18bp@gmail.com']

    # Crea el objeto EmailMessage con contenido HTML
    email = EmailMessage(subject, html_content, from_email, to_email)
    email.content_subtype = "html"  # Especifica el tipo de contenido como HTML

    try:
        # Envía el correo electrónico
        email.send()
        print("Correo electrónico enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")