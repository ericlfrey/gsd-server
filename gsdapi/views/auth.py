from rest_framework.decorators import api_view
from rest_framework.response import Response
from gsdapi.models import Client


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments: request -- The full HTTP request object
    '''
    uid = request.META['HTTP_AUTHORIZATION']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    client = Client.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if client is not None:
        data = {
            'id': client.id,
            'uid': client.uid,
            'first_name': client.first_name,
            'last_name': client.last_name
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments: request -- The full HTTP request object
    '''

    # Now save the user info in the gsdapi_client table
    client = Client.objects.create(
        uid=request.META['HTTP_AUTHORIZATION'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    # Return the client info to the client
    data = {
        'id': client.id,
        'uid': client.uid,
        'first_name': client.first_name,
        'last_name': client.last_name,
    }
    return Response(data)
