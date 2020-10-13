from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Vendor, Bidder
# Register your models here. (by sumit.luv)

admin.site.register(Vendor)

admin.site.register(Bidder)

