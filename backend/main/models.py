from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Suburb(models.Model):
    name = models.CharField(max_length=200)
    town = models.ForeignKey(Town, on_delete=models.PROTECT)

    def __str__(self):
        return "{}, {}".format(self.name, self.town)


class House(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Suburb, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    bedrooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pets_allowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"


class Agent(User):
    pass
