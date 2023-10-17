"""AppBuilder9000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Journal/', include('Journal.urls')),
    path('JournalBootstrap/', include('JournalBootstrap.urls')),
    path('DwarfFortGen/', include('DwarfFortGen.urls')),
    path('DeadByDaylight/', include('DeadByDaylight.urls')),
    path('HSDeckTracker/', include('HSDeckTracker.urls')),
    path('Sportsapp/', include('Sportsapp.urls')),
    path('LosoVision/', include('LosoVision.urls')),
    path('ItemsApp/', include('ItemsApp.urls')),
    path('Games/', include('Games.urls')),
    path('JA3Mercs/', include('JA3Mercs.urls')),
]
