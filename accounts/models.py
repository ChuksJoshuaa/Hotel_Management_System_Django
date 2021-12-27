from django.db import models
from PIL import Image
from django.core.files.storage import default_storage as storage


class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to="User/images", blank=True, null=True)
    phone_no = models.CharField(max_length=50)

    def __str__(self):
        return f"Customer: {self.username}"

    def save(self, *args, **kwargs):
        if not self.username and self.email:
            return

        super(Customer, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = "png"
            image.save(fh, format)
            fh.close()


class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Manager/images",  blank=True, null=True)
    phone_no = models.CharField(max_length=50)

    def __str__(self):
        return f"Room Manager: {self.username}"

    def save(self, *args, **kwargs):
        if not self.username and self.email:
            return

        super(Manager, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = 'png'
            image.save(fh, format)
            fh.close()