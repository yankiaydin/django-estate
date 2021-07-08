from django import forms
from .models import saleOffice, rentOffice, SaleOfficePhoto, RentOfficePhoto


class SaleOfficeForm(forms.ModelForm):
    class Meta:
        model = saleOffice
        fields = [
            "title",
            "location",
            "age",
            "sqm",
            "heating",
            "room",
            "room_type",
            "floor",
            "price",
            "detail",
            "contact",
        ]


class RentOfficeForm(forms.ModelForm):
    class Meta:
        model = rentOffice
        fields = [
            "title",
            "location",
            "age",
            "sqm",
            "heating",
            "room",
            "room_type",
            "floor",
            "pay_due",
            "price",
            "detail",
            "contact",
        ]


class RentOfficePhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = RentOfficePhoto
        fields = [
            "images",
        ]


class SaleOfficePhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = SaleOfficePhoto
        fields = [
            "images",
        ]
