from django.contrib import admin
from .models import saleOffice, rentOffice, SaleOfficePhoto, RentOfficePhoto

# Register your models here.


class SaleOfficePhotoAdmin(admin.StackedInline):
    model = SaleOfficePhoto


@admin.register(saleOffice)
class SaleOfficeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "location", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [SaleOfficePhotoAdmin]

    class Meta:
        model = saleOffice


@admin.register(SaleOfficePhoto)
class SaleOfficePhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = SaleOfficePhoto


class RentOfficePhotoAdmin(admin.StackedInline):
    model = RentOfficePhoto


@admin.register(rentOffice)
class RentHouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "location", "price", "date"]
    list_display_links = ["title", "owner"]
    inlines = [RentOfficePhotoAdmin]

    class Meta:
        model = rentOffice


@admin.register(RentOfficePhoto)
class RentOfficePhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "sale_owner"]
    list_display_links = ["post", "id"]

    class Meta:
        model = RentOfficePhoto
