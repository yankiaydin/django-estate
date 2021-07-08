from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import OptionForm
from vehicle.models import ForsaleCar, RentalCar, RentCarPhoto, SaleCarPhoto
from vehicle.forms import SaleCarForm, RentalCarForm, RentCarPhotoForm, SaleCarPhotoForm
from housing.models import saleHouse, rentHouse, SaleHousePhoto, RentHousePhoto
from housing.forms import (
    SaleHouseForm,
    RentHouseForm,
    RentHousePhotoForm,
    SaleHousePhotoForm,
)
from office.forms import (
    SaleOfficeForm,
    RentOfficeForm,
    RentOfficePhotoForm,
    SaleOfficePhotoForm,
)
from office.models import saleOffice, rentOffice, SaleOfficePhoto, RentOfficePhoto
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required(login_url="/member/login/")
def advert_add(request):
    if request.method == "POST":
        option = request.POST.get("advert_option")
        if option == "vehicle-sale":
            return redirect("vehicle_sale")
        elif option == "vehicle-rent":
            return redirect("vehicle_rent")
        elif option == "estate-sale":
            return redirect("housing_sale")
        elif option == "estate-rent":
            return redirect("housing_rent")
        elif option == "office-sale":
            return redirect("office_sale")
        elif option == "office-rent":
            return redirect("office_rent")

    form = OptionForm()
    return render(request, "advert_add.html", {"form": form})


@login_required(login_url="/member/login/")
def vehicle_sale(request):
    if request.method == "POST":
        form = SaleCarForm(request.POST or None)
        photo_form = SaleCarForm(request.FILES or None)
        newCar = form.save(commit=False)
        newCar.owner = request.user
        newCar.save()
        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = SaleCarPhoto.objects.create(post=newCar, images=file)
                newPhoto.save()
        return HttpResponseRedirect(
            reverse("vehicle:sale_detail_page", args=[newCar.id])
        )
    form = SaleCarForm()
    photo_form = SaleCarPhotoForm()
    type = "vehicle-sale"
    return render(
        request,
        "vehicle/vehicle_edit.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def vehicle_rent(request):
    if request.method == "POST":
        form = RentalCarForm(request.POST or None)
        photo_form = RentCarPhotoForm(request.FILES or None)
        newCar = form.save(commit=False)
        newCar.owner = request.user
        newCar.save()
        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = RentCarPhoto.objects.create(post=newCar, images=file)
                newPhoto.save()
        return HttpResponseRedirect(
            reverse("vehicle:rental_detail_page", args=[newCar.id])
        )
    form = RentalCarForm()
    photo_form = RentCarPhotoForm()
    type = "vehicle-rental"
    return render(
        request,
        "vehicle/vehicle_edit.html",
        {"form": form, "photo_form": photo_form, "type": type},
    )


@login_required(login_url="/member/login/")
def housing_sale(request):
    if request.method == "POST":
        form = SaleHouseForm(request.POST or None)
        photo_form = SaleHousePhotoForm(request.FILES or None)

        newRoom = form.save(commit=False)
        newRoom.owner = request.user
        newRoom.save()

        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = SaleHousePhoto.objects.create(post=newRoom, images=file)
                newPhoto.save()
        return HttpResponseRedirect(reverse("housing:sale_detail", args=[newRoom.id]))
    form = SaleHouseForm()
    photo_form = SaleHousePhotoForm()
    type = "housing-sale"
    return render(
        request,
        "housing/housing_edit.html",
        {"type": type, "form": form, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def housing_rent(request):
    if request.method == "POST":
        form = RentHouseForm(request.POST or None)
        photo_form = RentHousePhotoForm(request.FILES or None)

        newRoom = form.save(commit=False)
        newRoom.owner = request.user
        newRoom.save()

        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = RentHousePhoto.objects.create(post=newRoom, images=file)
                newPhoto.save()
        return HttpResponseRedirect(reverse("housing:rent_detail", args=[newRoom.id]))
    form = RentHouseForm()
    photo_form = RentHousePhotoForm()
    type = "housing-rent"
    return render(
        request,
        "housing/housing_edit.html",
        {"type": type, "form": form, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def office_sale(request):
    if request.method == "POST":
        form = SaleOfficeForm(request.POST or None)
        photo_form = SaleOfficePhotoForm(request.FILES or None)

        newOffice = form.save(commit=False)
        newOffice.owner = request.user
        newOffice.save()

        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = SaleOfficePhoto.objects.create(post=newOffice, images=file)
                newPhoto.save()
        return HttpResponseRedirect(reverse("office:sale_detail", args=[newOffice.id]))
    form = SaleOfficeForm()
    photo_form = SaleOfficePhotoForm()
    type = "office-sale"
    return render(
        request,
        "office/office_edit.html",
        {"type": type, "form": form, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def office_rent(request):
    if request.method == "POST":
        form = RentOfficeForm(request.POST or None)
        photo_form = RentOfficePhotoForm(request.FILES or None)

        newOffice = form.save(commit=False)
        newOffice.owner = request.user
        newOffice.save()

        if photo_form:
            for file in request.FILES.getlist("images"):
                newPhoto = RentOfficePhoto.objects.create(post=newOffice, images=file)
                newPhoto.save()
        return HttpResponseRedirect(reverse("office:rent_detail", args=[newOffice.id]))
    form = RentOfficeForm()
    photo_form = RentOfficePhotoForm()
    type = "office-rent"
    return render(
        request,
        "office/office_edit.html",
        {"type": type, "form": form, "photo_form": photo_form},
    )


def search_results(request):
    if request.method == "POST":
        hashtag = request.POST.get("hashtag")
        rent_car = RentalCar.objects.filter(location__startswith=hashtag)
        sale_car = ForsaleCar.objects.filter(location__startswith=hashtag)
        rent_home = rentHouse.objects.filter(location__startswith=hashtag)
        sale_home = saleHouse.objects.filter(location__startswith=hashtag)
        rent_office = rentOffice.objects.filter(location__startswith=hashtag)
        sale_office = saleOffice.objects.filter(location__startswith=hashtag)
        context = {
            "rent_car": rent_car,
            "sale_car": sale_car,
            "rent_home": rent_home,
            "sale_home": sale_home,
            "rent_office": rent_office,
            "sale_office": sale_office,
        }
        messages.warning(request, "No advert in this location!")
        return render(request, "results.html", {"context": context, "hashtag": hashtag})
    return render(request, "results.html")
