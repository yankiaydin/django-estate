from django.contrib import admin
from .models import ForsaleCar, RentalCar, RentCarPhoto, SaleCarPhoto

# Register your models here.


class SalePhotoAdmin(admin.StackedInline):
    model = SaleCarPhoto


@admin.register(ForsaleCar)
class ForsaleCarAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [SalePhotoAdmin]

    class Meta:
        model = ForsaleCar


@admin.register(SaleCarPhoto)
class SaleCarPhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = SaleCarPhoto


class RentalPhotoAdmin(admin.StackedInline):
    model = RentCarPhoto


@admin.register(RentalCar)
class RentalCarAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [RentalPhotoAdmin]

    class Meta:
        model = RentalCar


@admin.register(RentCarPhoto)
class RentalPhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = SaleCarPhoto
