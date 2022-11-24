from django.contrib import admin

from users.models import Vendor, Product, Store

admin.site.register([Product, Store, Vendor])
