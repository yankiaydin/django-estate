from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from vehicle.models import ForsaleCar, RentalCar
from housing.models import saleHouse, rentHouse
from office.models import saleOffice, rentOffice

# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST.get("password") == request.POST.get("confirmation"):
                name = form.cleaned_data.get("username")
                mail = form.cleaned_data.get("email")
                first = form.cleaned_data.get("first_name")
                last = form.cleaned_data.get("last_name")
                newUser = User.objects.create(
                    username=name, email=mail, first_name=first, last_name=last
                )
                newUser.set_password(form.cleaned_data.get("password"))
                newUser.save()
                login(request, newUser)
                return redirect("home")
            else:
                return HttpResponse("Hata")
    form = UserForm()
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("Hata")
    form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")


def profile_detail(request, id=id):
    mitglied = User.objects.get(id=id)
    car_sales = ForsaleCar.objects.filter(owner=mitglied)
    car_rents = RentalCar.objects.filter(owner=mitglied)
    home_sales = saleHouse.objects.filter(owner=mitglied)
    home_rents = rentHouse.objects.filter(owner=mitglied)
    office_rents = rentOffice.objects.filter(owner=mitglied)
    office_sales = saleOffice.objects.filter(owner=mitglied)
    return render(
        request,
        "profile.html",
        {
            "mitglied": mitglied,
            "car_sales": car_sales,
            "car_rents": car_rents,
            "home_sales": home_sales,
            "home_rents": home_rents,
            "office_rents": office_rents,
            "office_sales": office_sales,
        },
    )


def edit_profile(request, id=id):
    profile = get_object_or_404(User, id=id)
    form = UserForm(instance=profile)
    return render(request, "profile_edit.html", {"form": form})
