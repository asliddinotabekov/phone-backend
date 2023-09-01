from django.db import models
class Attribute(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.url

class Offer(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    merchant = models.CharField(max_length=100)
    attributes = models.ManyToManyField(Attribute)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.name