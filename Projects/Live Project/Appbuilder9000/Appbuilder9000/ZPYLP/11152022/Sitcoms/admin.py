from django.contrib import admin

from .models import Sitcom, SitcomCharacter, WeatherMoment

admin.site.register(Sitcom)

admin.site.register(SitcomCharacter)

admin.site.register(WeatherMoment)
