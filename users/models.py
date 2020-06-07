from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #CASCADE means if user is deleted, also delete the posts by the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Pillow must be installed, a library that works with image in Python
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        elif img.height < 100 or img.width < 100:
            output_size = (img.height, img.width)
            img.thumbnail(output_size)
            img.save(self.image.path)
