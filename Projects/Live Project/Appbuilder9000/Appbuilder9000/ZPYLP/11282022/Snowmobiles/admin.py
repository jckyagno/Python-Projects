from django.contrib import admin

# Register your models here.
from .models import Snowmobile, Dealer

admin.site.register(Snowmobile)
admin.site.register(Dealer)
