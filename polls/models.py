from django.db import models


class Student(models.Model):
    def images(instance, filename):
        return '/'.join([images, str(instance.name), filename])
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    email_id = models.EmailField()
    image = models.ImageField(upload_to="images", null="True", blank="True")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name
