from django.urls import path
from . import views

app_name = "vehicle"

urlpatterns = [
    path("", views.vehicles_page, name="vehicle_page"),
    path("detail/s/<int:id>", views.sale_detail_page, name="sale_detail_page"),
    path("detail/r/<int:id>", views.rental_detail_page, name="rental_detail_page"),
    path("update/r/<int:id>", views.update_rent, name="update_rent"),
    path("update/s/<int:id>", views.update_sale, name="update_sale"),
    path("delete/s/<int:id>", views.delete_sale, name="delete_sale"),
    path("delete/r/<int:id>", views.delete_rent, name="delete_rent"),
]
