from django.contrib import admin

# Register your models here.
from .models import Account, Evaluation, Approach

admin.site.register(Account)
admin.site.register(Approach)
admin.site.register(Evaluation)
