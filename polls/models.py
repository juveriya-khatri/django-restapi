from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    email_id = models.EmailField()

    def __str__(self):
        return self.name