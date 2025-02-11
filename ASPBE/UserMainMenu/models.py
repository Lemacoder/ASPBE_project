from django.db import models
from HoldingMainMenu.models import Venues
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    account_type = models.IntegerField()
    auntificatiuon = models.BooleanField()


class WishList(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    venue = models.OneToOneField(Venues, on_delete=models.CASCADE)