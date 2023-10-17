from django.contrib import admin

# Register your models here.
from .models import Character, Comment, Quote

admin.site.register(Character)
admin.site.register(Comment)
admin.site.register(Quote)
