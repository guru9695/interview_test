from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Vendor, Bidder

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['company_name', 
                  'address_line1',
                  'address_line2',
                  'mobile',
                  'telophone',
                  'city',
                  'portal_zip',
                  'state',
                  'country',
                  'user']

class BidderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bidder
        fields = ['company_name', 
                  'address_line1',
                  'address_line2',
                  'mobile',
                  'telophone',
                  'city',
                  'portal_zip',
                  'state',
                  'country',
                  'user']


