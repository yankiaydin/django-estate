from django.contrib import admin
from .models import saleHouse, rentHouse, SaleHousePhoto, RentHousePhoto

# Register your models here.


class SaleHousePhotoAdmin(admin.StackedInline):
    model = SaleHousePhoto


@admin.register(saleHouse)
class SaleHouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "location", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [SaleHousePhotoAdmin]

    class Meta:
        model = saleHouse


@admin.register(SaleHousePhoto)
class SaleHousePhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = SaleHousePhoto


class RentHousePhotoAdmin(admin.StackedInline):
    model = RentHousePhoto


@admin.register(rentHouse)
class RentHouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "location", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [RentHousePhotoAdmin]

    class Meta:
        model = rentHouse


@admin.register(RentHousePhoto)
class RentHousePhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = RentHousePhoto
