from django.db import models



class Holding(models.Model):
    name = models.CharField(max_length=255) 
    pass


class Emploees(models.Model):
    user_id = models.OneToOneField('UserMainMenu.Users', on_delete=models.CASCADE)
    holding_id = models.OneToOneField(Holding, on_delete=models.CASCADE)
    rooles = models.IntegerField()


class Venues(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    square = models.IntegerField()
    wardrobe = models.BooleanField()
    parking = models.BooleanField()
    status = models.IntegerField()

    def __str__(self):
        return self.name


class Photos(models.Model):
    venue = models.ForeignKey(Venues, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='holdings/')