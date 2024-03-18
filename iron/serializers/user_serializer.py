import json

def users_serializer(users):
    """
    user serializer.
    """
    users_serialized = []

    for user in users:
        user_data = {
            'id': user.id,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'email': user.email,
            'contact': user.contact,
            'subject': user.subject,
            'description': user.description,
            'projects': user.projects,
            'professions': user.professions,
            'hear_about_us': user.hear_about_us
        }
        users_serialized.append(user_data)

    return json.dumps(users_serialized)