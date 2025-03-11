from django.db import models
from HoldingMainMenu.models import Venues
from django.conf import settings

# Create your models here.




"""class WishList(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    venue_id = models.OneToOneField(Venues, on_delete=models.CASCADE)
    """