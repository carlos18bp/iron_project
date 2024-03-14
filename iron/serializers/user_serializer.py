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
        }
        users_serialized.append(user_data)

    return json.dumps(users_serialized)