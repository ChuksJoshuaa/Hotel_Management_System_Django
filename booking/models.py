from django.db import models
from accounts.models import Manager, Customer
from PIL import Image
from django.core.files.storage import default_storage as storage

class News(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "News"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name_plural = "Contact"

class Rooms(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=1000.00)
    no_of_days_advance = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(default='room.jpg', upload_to='User/images/', null=False, blank=False)


    def __str__(self):
        return "Room No: "+ str(self.id)

    class Meta:
        verbose_name_plural = "Rooms"

    def save(self, *args, **kwargs):
        if not self.room_no and self.room_type:
            return

        super(Rooms, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = "png"
            image.save(fh, format)
            fh.close()


class Booking(models.Model):
    room_no = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Booking ID: " + str(self.id)

    class Meta:
        verbose_name_plural = "Booking"

    @property
    def is_past_due(self):
        return self.start_day > self.end_day


