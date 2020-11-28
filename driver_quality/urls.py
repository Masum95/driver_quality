"""driver_quality URL Configuration

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
# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('supply_order/', include('supply_order.urls', namespace='supply_order')),
# ]


from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import os
from dotenv import load_dotenv
load_dotenv()

# schema view is used to automatically generate swagger documentation view
# to learn more, view the drf-yasg documentation.
schema_view = get_schema_view(
   openapi.Info(
      title="Driver Quality Database API",
      default_version='v1',
      description="A feedback service for drivers",
   ),
   public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('supply_order/', include('supply_order.urls', namespace='supply_order')),
]