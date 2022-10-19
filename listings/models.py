from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'


    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    #like_new = models.fields.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'Records'
        CLOTHING = 'Clothing'
        POSTERS = 'Posters'
        MISCELLANEOUS = 'Miscellaneous'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    type = models.fields.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title
