from django.urls import path
from . import views

app_name = "office"

urlpatterns = [
    path("", views.office_page, name="office_page"),
    path("detail/r/<int:id>", views.office_rent_detail, name="rent_detail"),
    path("detail/s/<int:id>", views.office_sale_detail, name="sale_detail"),
    path("update/r/<int:id>", views.update_rent, name="update_rent"),
    path("update/s/<int:id>", views.update_sale, name="update_sale"),
    path("delete/s/<int:id>", views.delete_sale, name="delete_sale"),
    path("delete/r/<int:id>", views.delete_rent, name="delete_rent"),
]
