from django.db import models
from django.contrib import admin


class RentalCar(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title of your Advertisement", max_length=100)
    price = models.CharField(verbose_name="Daily Price", max_length=15, help_text="USD")
    location = models.CharField(verbose_name="Location", max_length=30)
    brand = models.CharField(verbose_name="Brand", max_length=20)
    model = models.CharField(verbose_name="Model", max_length=50)
    year = models.CharField(verbose_name="Year", max_length=4)
    fuel_option = [
        ("Oil", "Oil"),
        ("Diesel", "Diesel"),
        ("LPG", "LPG"),
        ("Hybrid", "Hybrid"),
    ]
    fuel = models.CharField(verbose_name="Fuel", choices=fuel_option, max_length=20)
    gear_option = [("Auto", "Auto"), ("Manuel", "Manuel")]
    gear = models.CharField(verbose_name="Gear", choices=gear_option, max_length=20)
    bio = models.TextField(verbose_name="Explanation", blank=True)
    contact = models.CharField(
        verbose_name="Contact Info", max_length=40, help_text="Mobile Phone"
    )
    date = models.DateTimeField(verbose_name="Proclamation Date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class RentCarPhoto(models.Model):
    post = models.ForeignKey(RentalCar, on_delete=models.CASCADE)
    images = models.ImageField(
        verbose_name="Upload Images", upload_to="rentalcars/", blank=True, null=True
    )

    def __str__(self):
        return ("%s %s %s" % (self.post.owner, "--", self.post)).upper()

    @admin.display(description="Advert Owner")
    def sale_owner(self):
        return "%s" % (self.post.owner)


class ForsaleCar(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title of your Advertisement", max_length=100)
    price = models.CharField(verbose_name="Price", max_length=15, help_text="USD")
    location = models.CharField(verbose_name="Location", max_length=30)
    brand = models.CharField(verbose_name="Brand", max_length=20)
    model = models.CharField(verbose_name="Model", max_length=50)
    year = models.CharField(verbose_name="Year", max_length=4)
    fuel_option = [
        ("Oil", "Oil"),
        ("Diesel", "Diesel"),
        ("LPG", "LPG"),
        ("Hybrid", "Hybrid"),
    ]
    fuel = models.CharField(verbose_name="Fuel", choices=fuel_option, max_length=20)
    exchange = models.BooleanField(verbose_name="Exchange Available", default=None)
    gear_option = [("Auto", "Auto"), ("Manuel", "Manuel")]
    gear = models.CharField(verbose_name="Gear", choices=gear_option, max_length=20)
    statue_option = [("First Hand", "First Hand"), ("Second Hand", "Second Hand")]
    statue = models.CharField(
        verbose_name="Statue", choices=statue_option, max_length=30
    )
    bio = models.TextField(verbose_name="Explanation", blank=True)
    contact = models.CharField(
        verbose_name="Contact Info", max_length=40, help_text="Mobile Phone"
    )
    date = models.DateTimeField(verbose_name="Proclamation Date", auto_now_add=True)

    def __str__(self):
        return self.title


class SaleCarPhoto(models.Model):
    post = models.ForeignKey(ForsaleCar, on_delete=models.CASCADE)
    images = models.ImageField(
        verbose_name="Upload Images", blank=True, upload_to="forsalecars/", null=True
    )

    def __str__(self):
        return ("%s %s %s" % (self.post.owner, "--", self.post)).upper()

    @admin.display(description="Advert Owner")
    def sale_owner(self):
        return "%s" % (self.post.owner)
