from django.db import models
from django.utils.text import slugify


class Town(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Suburb(models.Model):
    name = models.CharField(max_length=200, unique=True)
    town = models.ForeignKey(Town, on_delete=models.PROTECT)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.town)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class House(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.ForeignKey(Suburb, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    bedrooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pets_allowed = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Agent(User):
    pass
