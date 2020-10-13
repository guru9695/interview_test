from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Vendor, Bidder, TokenData
from .serializers import VendorSerializer, BidderSerializer
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
import json
# from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,

    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



def required_parameters(req_params, account_for=None):

    def inner(function):

        def wrapper(*args, **kwargs):
            for field in req_params:
                if field not in args[0].data:
                    return Response({
                        "code": 410,
                        "detail": "Must provide {missing_key} when creating a {account_for} account."
                                .format(missing_key=field, account_for=account_for)
                    })
            return function(*args, **kwargs)
        return wrapper

    return inner

def allowed_parameters(allowed_params, account_for=None):

    def inner(function):

        def wrapper(*args, **kwargs):
            if set(args[0].data.keys())-set(allowed_params):
                return Response({
                    "code": 411,
                    "detail": "Please remove extra parameters"
                })
            return function(*args, **kwargs)
        return wrapper

    return inner



@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@required_parameters(['first_name', 
                      'last_name', 
                      'username', 
                      'password',
                      'email', 
                      'company_name',
                      'address_line2',
                      'telophone',
                      'mobile',
                      'city',
                      'portal_zip',
                      'state',
                      'country',
                       'address_line1'], "VENDOR")
@allowed_parameters(['first_name', 
                     'last_name', 
                     'username', 
                     'email', 
                     'company_name', 
                     'address_line1',
                     'address_line2',
                     'mobile', 
                     'city',
                     'portal_zip',
                     'telophone',
                     'state',
                     'user',
                     'password',
                     'country',
                     'email'], "VENDOR")
def vendor_signup(request):
    if request.method == 'GET':
        posts = Vendor.objects.all()
        serializer = VendorSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if User.objects.filter(username=request.data.get('username')):
            return Response({
                'code': 412,
                'detail': "User already exists"
            })
        user_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'username': request.data.get('username'),
            'email': request.data.get('email')
        }
        user = User(**user_data)
        user.set_password(request.data.get('password'))
        res = user.save()
        data = {
            'company_name': request.data.get('company_name') if request.data.get('company_name') else None, 
            'address_line1': request.data.get('address_line1') if request.data.get('address_line1') else None,
            'address_line2': request.data.get('address_line2') if request.data.get('address_line2') else None, 
            'mobile': request.data.get('mobile') if request.data.get('mobile') else None, 
            'city': request.data.get('city') if request.data.get('city') else None, 
            'portal_zip': request.data.get('portal_zip') if request.data.get('portal_zip') else None, 
            'telophone': request.data.get('telophone') if request.data.get('telophone') else None, 
            'state': request.data.get('state') if request.data.get('state') else None,  
            'country': request.data.get('country') if request.data.get('country') else None,  
            'email': request.data.get('email') if request.data.get('email') else None,  
            
            'user': user.pk
        }
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            my_vendor_group = Group.objects.get_or_create(name='VENDOR')
            my_vendor_group[0].user_set.add(user)
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)


def home_view(request):
    return render(request,'index.html')


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@required_parameters(['first_name', 
                      'last_name', 
                      'username', 
                      'password',
                      'email', 
                      'company_name',
                      'address_line2',
                      'telophone',
                      'mobile',
                      'city',
                      'portal_zip',
                      'state',
                      'country',
                       'address_line1'], "BIDDER")
@allowed_parameters(['first_name', 
                     'last_name', 
                     'username', 
                     'email', 
                     'company_name', 
                     'address_line1',
                     'address_line2',
                     'mobile', 
                     'city',
                     'portal_zip',
                     'telophone',
                     'state',
                     'user',
                     'password',
                     'country',
                     'email'], "BIDDER")
def bidder_signup(request):
    if request.method == 'GET':
        posts = Bidder.objects.all()
        serializer = BidderSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if User.objects.filter(username=request.data.get('username')):
            return Response({
                'code': 412,
                'detail': "User already exists"
            })
        user_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'username': request.data.get('username'),
            'email': request.data.get('email')
        }
        user = User(**user_data)
        user.set_password(request.data.get('password'))
        res = user.save()
        data = {
            'company_name': request.data.get('company_name') if request.data.get('company_name') else None, 
            'address_line1': request.data.get('address_line1') if request.data.get('address_line1') else None,
            'address_line2': request.data.get('address_line2') if request.data.get('address_line2') else None, 
            'mobile': request.data.get('mobile') if request.data.get('mobile') else None, 
            'city': request.data.get('city') if request.data.get('city') else None, 
            'portal_zip': request.data.get('portal_zip') if request.data.get('portal_zip') else None, 
            'telophone': request.data.get('telophone') if request.data.get('telophone') else None, 
            'state': request.data.get('state') if request.data.get('state') else None,  
            'country': request.data.get('country') if request.data.get('country') else None,  
            'email': request.data.get('email') if request.data.get('email') else None,  
            
            'user': user.pk
        }
        serializer = BidderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            my_BIDDER_group = Group.objects.get_or_create(name='BIDDER')
            my_BIDDER_group[0].user_set.add(user)
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
@required_parameters(['username', 'password'], "vendor")
def vendor_login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
       # user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        # if not TeacherExtra.objects.filter(user=user.id)[0].status:
        #         return Response({'error': 'User Not Approved'},
        #                             status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        check_usr = user.groups.filter(name='VENDOR').exists()
        if not check_usr:
            return Response({'error': 'Invalid User'},
                            status=HTTP_404_NOT_FOUND)
        TokenData.objects.filter(user=user.id).delete()
        token_data = {
        'user': user,
        'token': token,
        'start_date': "2020-10-12",
        'expiry_date': "2020-10-14",
        'user_type': "vendor"
        }
        tok_data = TokenData(**token_data)
        tok_data.save()
        
        print("tokeeeen", token)
        return Response({
            'code': 200,
            'detail': "Login succesfully",
            "user_type": "vendor",
            "token": token.key
            }, status=HTTP_200_OK)
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
@required_parameters(['username', 'password'], "bidder")
def bidder_login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
       # user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        # if not TeacherExtra.objects.filter(user=user.id)[0].status:
        #         return Response({'error': 'User Not Approved'},
        #                             status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        check_usr = user.groups.filter(name='BIDDER').exists()
        if not check_usr:
            return Response({'error': 'Invalid User'},
                            status=HTTP_404_NOT_FOUND)
        TokenData.objects.filter(user=user.id).delete()
        token_data = {
        'user': user,
        'token': token,
        'start_date': "2020-06-04",
        'expiry_date': "2020-06-20",
        'user_type': "bidder"
        }
        tok_data = TokenData(**token_data)
        tok_data.save()
        
        print("tokeeeen", token)
        return Response({
            'code': 200,
            'detail': "Login succesfully",
            "user_type": "bidder",
            "token": token.key
            }, status=HTTP_200_OK)