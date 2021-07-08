"""estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("results/", views.search_results, name="results"),
    path("member/", include("member.urls")),
    path("vehicle/", include("vehicle.urls")),
    path("housing/", include("housing.urls")),
    path("office/", include("office.urls")),
    path("advert/add/", views.advert_add, name="advert_add"),
    path("advert/vehicle/sale/", views.vehicle_sale, name="vehicle_sale"),
    path("advert/vehicle/rent/", views.vehicle_rent, name="vehicle_rent"),
    path("advert/housing/rent/", views.housing_rent, name="housing_rent"),
    path("advert/housing/sale/", views.housing_sale, name="housing_sale"),
    path("advert/office/rent/", views.office_rent, name="office_rent"),
    path("advert/office/sale/", views.office_sale, name="office_sale"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
