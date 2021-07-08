from django import forms
from .models import ForsaleCar, RentalCar, RentCarPhoto, SaleCarPhoto


class SaleCarForm(forms.ModelForm):
    class Meta:
        model = ForsaleCar
        fields = [
            "title",
            "price",
            "location",
            "brand",
            "model",
            "year",
            "fuel",
            "exchange",
            "gear",
            "statue",
            "bio",
            "contact",
        ]


class RentalCarForm(forms.ModelForm):
    class Meta:
        model = RentalCar
        fields = [
            "title",
            "price",
            "location",
            "brand",
            "model",
            "year",
            "fuel",
            "gear",
            "bio",
            "contact",
        ]


class RentCarPhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = RentCarPhoto
        fields = [
            "images",
        ]


class SaleCarPhotoForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = SaleCarPhoto
        fields = [
            "images",
        ]
