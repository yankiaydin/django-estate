from django.db import models
from django.contrib import admin

# Create your models here.


class saleOffice(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title of your Advertisement", max_length=100)
    location = models.CharField(verbose_name="Location", max_length=100)
    age = models.IntegerField(verbose_name="Age of your Building")
    sqm = models.CharField(
        verbose_name="Area/Squaremeter", max_length=5, help_text="m²"
    )
    heating_options = [
        ("Central System", "Central System"),
        ("Solar Panel", "Solar Panel"),
        ("Air Conditioner", "Air Conditioner"),
        ("Electricity", "Electricity"),
        ("None", "None"),
    ]
    heating = models.CharField(
        verbose_name="Heating Type", choices=heating_options, max_length=30
    )
    room = models.CharField(verbose_name="Number of your Rooms", max_length=5)
    type_options = [("Suite", "Suite"), ("Villa", "Villa"), ("Building", "Building")]
    room_type = models.CharField(
        verbose_name="Type of your estate", choices=type_options, max_length=30
    )
    floor = models.IntegerField(verbose_name="Level/floor of your room")
    pay_due = models.CharField(
        verbose_name="Montly Subscription Fee", max_length=5, help_text="USD"
    )
    price = models.CharField(verbose_name="Price", max_length=15, help_text="USD")
    detail = models.TextField(verbose_name="Explanation", blank=True)
    contact = models.CharField(
        verbose_name="Contact Info", max_length=40, help_text="Mobile Phone"
    )
    date = models.DateTimeField(verbose_name="Proclamation Date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class SaleOfficePhoto(models.Model):
    post = models.ForeignKey(saleOffice, on_delete=models.CASCADE)
    images = models.ImageField(
        verbose_name="Upload Images", upload_to="saleoffices/", blank=True, null=True
    )

    def __str__(self):
        return ("%s %s %s" % (self.post.owner, "--", self.post)).upper()

    @admin.display(description="Advert Owner")
    def sale_owner(self):
        return "%s" % (self.post.owner)


class rentOffice(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title of your Advertisement", max_length=100)
    location = models.CharField(verbose_name="Location", max_length=100)
    age = models.IntegerField(verbose_name="Age of your Building")
    sqm = models.CharField(
        verbose_name="Area/Squaremeter", max_length=5, help_text="m²"
    )
    heating_options = [
        ("Central System", "Central System"),
        ("Solar Panel", "Solar Panel"),
        ("Air Conditioner", "Air Conditioner"),
        ("Electricity", "Electricity"),
        ("None", "None"),
    ]
    heating = models.CharField(
        verbose_name="Heating Type", choices=heating_options, max_length=30
    )
    room = models.CharField(verbose_name="Number of your Rooms", max_length=5)
    type_options = [("Suite", "Suite"), ("Villa", "Villa"), ("Building", "Building")]
    room_type = models.CharField(
        verbose_name="Type of your estate", choices=type_options, max_length=30
    )
    floor = models.IntegerField(verbose_name="Level/floor of your room")
    pay_due = models.CharField(
        verbose_name="Montly Subscription Fee", max_length=5, help_text="USD"
    )
    price = models.CharField(
        verbose_name="Monthly Price", max_length=15, help_text="USD"
    )
    detail = models.TextField(verbose_name="Explanation", blank=True)
    contact = models.CharField(
        verbose_name="Contact Info", max_length=40, help_text="Mobile Phone"
    )
    date = models.DateTimeField(verbose_name="Proclamation Date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class RentOfficePhoto(models.Model):
    post = models.ForeignKey(rentOffice, on_delete=models.CASCADE)
    images = models.ImageField(
        verbose_name="Upload Images", upload_to="rentoffices/", blank=True, null=True
    )

    def __str__(self):
        return ("%s %s %s" % (self.post.owner, "--", self.post.title)).upper()

    @admin.display(description="Advert Owner")
    def sale_owner(self):
        return "%s" % (self.post.owner)
