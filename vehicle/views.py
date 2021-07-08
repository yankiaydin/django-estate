from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import ForsaleCar, RentalCar, RentCarPhoto, SaleCarPhoto
from .forms import SaleCarForm, RentalCarForm, RentCarPhotoForm, SaleCarPhotoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def vehicles_page(request):
    rents = RentalCar.objects.all()
    sales = ForsaleCar.objects.all()
    sphoto = SaleCarPhoto.objects.filter(post=sales[1])
    sphoto2 = SaleCarPhoto.objects.filter(post=sales[2])
    sphoto3 = SaleCarPhoto.objects.filter(post=sales[3])
    sphoto4 = SaleCarPhoto.objects.filter(post=sales[4])
    rphoto = RentCarPhoto.objects.filter(post=rents[1])
    rphoto2 = RentCarPhoto.objects.filter(post=rents[2])
    rphoto3 = RentCarPhoto.objects.filter(post=rents[3])
    rphoto4 = RentCarPhoto.objects.filter(post=rents[4])
    context = {
        "sphoto": sphoto,
        "sphoto2": sphoto2,
        "sphoto3": sphoto3,
        "sphoto4": sphoto4,
        "rphoto": rphoto,
        "rphoto2": rphoto2,
        "rphoto3": rphoto3,
        "rphoto4": rphoto4,
    }
    return render(
        request,
        "vehicle/vehicle.html",
        {"rents": rents, "sales": sales, "context": context},
    )


def sale_detail_page(request, id=id):
    vehicle = ForsaleCar.objects.get(id=id)
    vehicle_photos = SaleCarPhoto.objects.filter(post=vehicle)
    # as an admin or editor, you may change the id of the car to show best offers
    related_car = ForsaleCar.objects.get(id=7)
    related_car_photo = SaleCarPhoto.objects.filter(post=related_car)
    related_car2 = ForsaleCar.objects.get(id=6)
    related_car_photo2 = SaleCarPhoto.objects.filter(post=related_car2)
    related_car3 = ForsaleCar.objects.get(id=8)
    related_car_photo3 = SaleCarPhoto.objects.filter(post=related_car3)
    related_car4 = ForsaleCar.objects.get(id=10)
    related_car_photo4 = SaleCarPhoto.objects.filter(post=related_car4)
    context = {
        "related_car": related_car,
        "related_car_photo": related_car_photo,
        "related_car2": related_car2,
        "related_car_photo2": related_car_photo2,
        "related_car3": related_car3,
        "related_car_photo3": related_car_photo3,
        "related_car4": related_car4,
        "related_car_photo4": related_car_photo4,
    }
    return render(
        request,
        "vehicle/vehicle_sale_detail.html",
        {"vehicle": vehicle, "vehicle_photos": vehicle_photos, "context": context},
    )


def rental_detail_page(request, id=id):
    vehicle = RentalCar.objects.get(id=id)
    vehicle_photos = RentCarPhoto.objects.filter(post=vehicle)

    related_car = RentalCar.objects.get(id=82)
    related_car_photo = RentCarPhoto.objects.filter(post=related_car)
    related_car2 = ForsaleCar.objects.get(id=10)
    related_car_photo2 = SaleCarPhoto.objects.filter(post=related_car2)
    related_car3 = ForsaleCar.objects.get(id=9)
    related_car_photo3 = SaleCarPhoto.objects.filter(post=related_car3)
    related_car4 = RentalCar.objects.get(id=78)
    related_car_photo4 = RentCarPhoto.objects.filter(post=related_car4)
    context = {
        "related_car": related_car,
        "related_car_photo": related_car_photo,
        "related_car2": related_car2,
        "related_car_photo2": related_car_photo2,
        "related_car3": related_car3,
        "related_car_photo3": related_car_photo3,
        "related_car4": related_car4,
        "related_car_photo4": related_car_photo4,
    }

    return render(
        request,
        "vehicle/vehicle_rental_detail.html",
        {"vehicle": vehicle, "vehicle_photos": vehicle_photos, "context": context},
    )


@login_required(login_url="/member/login/")
def update_rent(request, id=id):
    if request.method == "POST":
        rent_car = get_object_or_404(RentalCar, id=id)
        form = RentalCarForm(request.POST or None, instance=rent_car)
        photos = RentCarPhoto.objects.filter(post=rent_car)
        photos.delete()
        photo_form = RentCarPhotoForm(request.FILES or None)
        if form.is_valid():
            updateCar = form.save(commit=False)
            updateCar.owner = request.user
            updateCar.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = RentCarPhoto.objects.create(
                        post=updateCar, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    rent_car = get_object_or_404(RentalCar, id=id)
    photos = RentCarPhoto.objects.filter(post=rent_car).first()
    form = RentalCarForm(instance=rent_car)
    photo_form = RentCarPhotoForm(instance=photos)
    type = "vehicle-rental"
    return render(
        request,
        "vehicle/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def update_sale(request, id=id):
    if request.method == "POST":
        sale_car = get_object_or_404(ForsaleCar, id=id)
        form = SaleCarForm(request.POST or None, instance=sale_car)
        photos = SaleCarPhoto.objects.filter(post=sale_car)
        photos.delete()
        photo_form = SaleCarPhotoForm(request.FILES or None)
        if form.is_valid():
            updateCar = form.save(commit=False)
            updateCar.owner = request.user
            updateCar.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = SaleCarPhoto.objects.create(
                        post=updateCar, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    sale_car = get_object_or_404(ForsaleCar, id=id)
    photos = SaleCarPhoto.objects.filter(post=sale_car).first()
    form = SaleCarForm(instance=sale_car)
    photo_form = SaleCarPhotoForm(instance=photos)
    type = "vehicle-sale"
    return render(
        request,
        "vehicle/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def delete_rent(request, id=id):
    rent_car = get_object_or_404(RentalCar, id=id)
    rent_car.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))


@login_required(login_url="/member/login/")
def delete_sale(request, id=id):
    sale_car = get_object_or_404(ForsaleCar, id=id)
    sale_car.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))
