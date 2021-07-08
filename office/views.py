from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from .models import saleOffice, rentOffice, SaleOfficePhoto, RentOfficePhoto
from .forms import (
    SaleOfficeForm,
    SaleOfficePhotoForm,
    RentOfficeForm,
    RentOfficePhotoForm,
)
from django.contrib.auth.decorators import login_required

# Create your views here.


def office_page(request):
    sales = saleOffice.objects.all()
    rents = rentOffice.objects.all()
    sphoto = SaleOfficePhoto.objects.filter(post=sales[1])
    sphoto2 = SaleOfficePhoto.objects.filter(post=sales[0])
    sphoto3 = SaleOfficePhoto.objects.filter(post=sales[3])
    sphoto4 = SaleOfficePhoto.objects.filter(post=sales[4])
    rphoto = RentOfficePhoto.objects.filter(post=rents[1])
    rphoto2 = RentOfficePhoto.objects.filter(post=rents[2])
    rphoto3 = RentOfficePhoto.objects.filter(post=rents[3])
    rphoto4 = RentOfficePhoto.objects.filter(post=rents[4])
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
        "office/offices.html",
        {"sales": sales, "rents": rents, "context": context},
    )


def office_sale_detail(request, id=id):
    office = get_object_or_404(saleOffice, id=id)
    office_photo = SaleOfficePhoto.objects.filter(post=office)
    # as an admin or editor, you may change the id of the car to show best offers
    instance1 = rentOffice.objects.get(id=1)
    instance1_photo = RentOfficePhoto.objects.filter(post=instance1)
    instance2 = saleOffice.objects.get(id=2)
    instance2_photo = SaleOfficePhoto.objects.filter(post=instance2)
    instance3 = saleOffice.objects.get(id=3)
    instance3_photo = SaleOfficePhoto.objects.filter(post=instance3)
    instance4 = rentOffice.objects.get(id=4)
    instance4_photo = RentOfficePhoto.objects.filter(post=instance4)
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
        "office/sale_detail.html",
        {"office": office, "office_photo": office_photo, "context": context},
    )


def office_rent_detail(request, id=id):
    office = get_object_or_404(rentOffice, id=id)
    office_photo = RentOfficePhoto.objects.filter(post=office)
    # as an admin or editor, you may change the id of the car to show best offers
    instance1 = rentOffice.objects.get(id=1)
    instance1_photo = RentOfficePhoto.objects.filter(post=instance1)
    instance2 = saleOffice.objects.get(id=2)
    instance2_photo = SaleOfficePhoto.objects.filter(post=instance2)
    instance3 = saleOffice.objects.get(id=3)
    instance3_photo = SaleOfficePhoto.objects.filter(post=instance3)
    instance4 = rentOffice.objects.get(id=4)
    instance4_photo = RentOfficePhoto.objects.filter(post=instance4)
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
        "office/rent_detail.html",
        {"office": office, "office_photo": office_photo, "context": context},
    )


@login_required(login_url="/member/login/")
def update_sale(request, id=id):
    if request.method == "POST":
        sale_office = get_object_or_404(saleOffice, id=id)
        form = SaleOfficeForm(request.POST or None, instance=sale_office)
        photos = SaleOfficePhoto.objects.filter(post=sale_office)
        photos.delete()
        photo_form = SaleHousePhotoForm(request.FILES or None)
        if form.is_valid():
            updateOffice = form.save(commit=False)
            updateOffice.owner = request.user
            updateOffice.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = SaleHousePhoto.objects.create(
                        post=updateOffice, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    sale_office = get_object_or_404(saleOffice, id=id)
    photos = SaleOfficePhoto.objects.filter(post=sale_office).first()
    form = SaleOfficeForm(instance=sale_office)
    photo_form = SaleOfficePhotoForm(instance=photos)
    type = "office-sale"
    return render(
        request,
        "office/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def update_rent(request, id=id):
    if request.method == "POST":
        rent_office = get_object_or_404(rentOffice, id=id)
        form = RentOfficeForm(request.POST or None, instance=rent_office)
        photos = RentOfficePhoto.objects.filter(post=rent_office)
        photos.delete()
        photo_form = RentOfficePhotoForm(request.FILES or None)
        if form.is_valid():
            updateOffice = form.save(commit=False)
            updateOffice.owner = request.user
            updateOffice.save()

            if photo_form:
                for file in request.FILES.getlist("images"):
                    updatePhoto = RentHousePhoto.objects.create(
                        post=updateOffice, images=file
                    )
                    updatePhoto.save()
            return HttpResponseRedirect(
                reverse("member:detail", args=[request.user.id])
            )

    rent_office = get_object_or_404(rentOffice, id=id)
    photos = RentOfficePhoto.objects.filter(post=rent_office).first()
    form = RentOfficeForm(instance=rent_office)
    photo_form = RentOfficePhotoForm(instance=photos)
    type = "office-rent"
    return render(
        request,
        "office/update.html",
        {"form": form, "type": type, "photo_form": photo_form},
    )


@login_required(login_url="/member/login/")
def delete_rent(request, id=id):
    rent_office = get_object_or_404(rentOffice, id=id)
    rent_office.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))


@login_required(login_url="/member/login/")
def delete_sale(request, id=id):
    sale_office = get_object_or_404(saleOffice, id=id)
    sale_office.delete()
    return HttpResponseRedirect(reverse("member:detail", args=[request.user.id]))
