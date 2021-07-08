from django import forms
from .models import saleHouse, rentHouse, SaleHousePhoto, RentHousePhoto


class SaleHouseForm(forms.ModelForm):
    class Meta:
        model = saleHouse
        fields = [
            "title",
            "location",
            "age",
            "sqm",
            "heating",
            "room",
            "room_type",
            "floor",
            "housekeeper",
            "pay_due",
            "mobel",
            "price",
            "detail",
            "contact",
        ]


class RentHouseForm(forms.ModelForm):
    class Meta:
        model = rentHouse
        fields = [
            "title",
            "location",
            "age",
            "sqm",
            "heating",
            "room",
            "room_type",
            "floor",
            "housekeeper",
            "pay_due",
            "mobel",
            "price",
            "detail",
            "contact",
        ]


class RentHousePhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = RentHousePhoto
        fields = [
            "images",
        ]


class SaleHousePhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = SaleHousePhoto
        fields = [
            "images",
        ]
