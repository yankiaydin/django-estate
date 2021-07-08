from django.db import models


class Option(models.Model):
    NOTICE_CHOICES = [
        (
            "Real-Estate",
            (
                ("estate-sale", "On Sale"),
                ("estate-rent", "Rental"),
            ),
        ),
        (
            "Vehicle",
            (
                ("vehicle-sale", "For Sale"),
                ("vehicle-rent", "Rental"),
            ),
        ),
        (
            "Office",
            (
                ("office-sale", "For Sale"),
                ("office-rent", "Rental"),
            ),
        ),
    ]
    advert_option = models.CharField(
        max_length=100,
        choices=NOTICE_CHOICES,
    )
