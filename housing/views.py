from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from .models import saleHouse, rentHouse, RentHousePhoto, SaleHousePhoto
from .forms import SaleHouseForm, SaleHousePhotoForm, RentHousePhotoForm, RentHouseForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def housing_page(request):
    sales = saleHouse.objects.all()
    rents = rentHouse.objects.all()
    sphoto = SaleHousePhoto.objects.filter(post=sales[1])
    sphoto2 = SaleHousePhoto.objects.filter(post=sales[2])
    sphoto3 = SaleHousePhoto.objects.filter(post=sales[3])
    sphoto4 = SaleHousePhoto.objects.filter(post=sales[4])
    rphoto = RentHousePhoto.objects.filter(post=rents[1])
    rphoto2 = RentHousePhoto.objects.filter(post=rents[2])
    rphoto3 = RentHousePhoto.objects.filter(post=rents[3])
    rphoto4 = RentHousePhoto.objects.filter(post=rents[4])
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
        "housing/housing.html",
        {"sales": sales, "rents": rents, "context": context},
    )


def housing_rent_detail(request, id=id):
    room = rentHouse.objects.get(id=id)
    room_photo = RentHousePhoto.objects.filter(post=room)
    # as an admin or editor, you may change the id of the car to show best offers
    instance1 = rentHouse.objects.get(id=7)
    instance1_photo = RentHousePhoto.objects.filter(post=instance1)
    instance2 = rentHouse.objects.get(id=8)
    instance2_photo = RentHousePhoto.objects.filter(post=instance2)
    instance3 = saleHouse.objects.get(id=10)
    instance3_photo = SaleHousePhoto.objects.filter(post=instance3)
    instance4 = saleHouse.objects.get(id=9)
    instance4_photo = SaleHousePhoto.objects.filter(post=instance4)
    context = {
        "instance1_photo": instance1_photo,
        "instance2_photo": instance2_photo,
        "instance3_photo": instance3_photo,
        "instance4_photo": instance4_photo,
        "instance1": instance1,
        "instance2": instance2,
        "instance3": instance3,
        "instance4": instance4,
    }
    return render(
        request,
        "housing/rental_detail.html",
        {"room": room, "room_photo": room_photo, "context": context},
    )


def housing_sale_detail(request, id=id):
    room = saleHouse.objects.get(id=id)
    room_photo = SaleHousePhoto.objects.filter(post=room)
    # as an admin or editor, you may change the id of the car to show best offers
    instance1 = rentHouse.objects.get(id=7)
    instance1_photo = RentHousePhoto.objects.filter(post=instance1)
    instance2 = rentHouse.objects.get(id=8)
    instance2_photo = RentHousePhoto.objects.filter(post=instance2)
    instance3 = saleHouse.objects.get(id=10)
    instance3_photo = SaleHousePhoto.objects.filter(post=instance3)
    instance4 = saleHouse.objects.get(id=9)
    instance4_photo = SaleHousePhoto.objects.filter(post=instance4)
    context = {
        "instance1_photo": instance1_photo,
        "instance2_photo": instance2_photo,
        "instance3_photo": instance3_photo,
        "instance4_photo": instance4_photo,
        "instance1": instance1,
        "instance2": instance2,
        "instance3": instance3,
        "instance4": instance4,
    }
    return render(
        request,
        "housing/sale_detail.html",
        {"room": room, "room_photo": room_photo, "context": context},
    )


@login_required(login_url="/member/login/")
def update_rent(request, id=id):
    if request.method == "POST":
        rent_home = get_object_or_404(rentHouse, id=id)
        form = RentHouseForm(request.POST or None, instance=rent_home)
        photos = RentHousePhoto.objects.filter(post=rent_home)
        photos.delete()
        photo_form = RentHousePhotoForm(request.FILES or None)
        if form.is_valid():
            updateHome = form.save(commit=False)
            updateHome.owner = request.user
            updateHome.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = RentHousePhoto.objects.create(
                        post=updateHome, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    rent_home = get_object_or_404(rentHouse, id=id)
    photos = RentHousePhoto.objects.filter(post=rent_home).first()
    form = RentHouseForm(instance=rent_home)
    photo_form = RentHousePhotoForm(instance=photos)
    type = "home-rental"
    return render(
        request,
        "housing/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def update_sale(request, id=id):
    if request.method == "POST":
        sale_home = get_object_or_404(saleHouse, id=id)
        form = SaleHouseForm(request.POST or None, instance=sale_home)
        photos = SaleHousePhoto.objects.filter(post=sale_home)
        photos.delete()
        photo_form = SaleHousePhotoForm(request.FILES or None)
        if form.is_valid():
            updateHome = form.save(commit=False)
            updateHome.owner = request.user
            updateHome.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = SaleHousePhoto.objects.create(
                        post=updateHome, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    sale_home = get_object_or_404(saleHouse, id=id)
    photos = SaleHousePhoto.objects.filter(post=sale_home).first()
    form = SaleHouseForm(instance=sale_home)
    photo_form = SaleHousePhotoForm(instance=photos)
    type = "home-sale"
    return render(
        request,
        "housing/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def delete_rent(request, id=id):
    rent_home = get_object_or_404(rentHouse, id=id)
    rent_home.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))


@login_required(login_url="/member/login/")
def delete_sale(request, id=id):
    sale_home = get_object_or_404(saleHouse, id=id)
    sale_home.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))
