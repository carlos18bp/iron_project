from django.db import models

class User(models.Model):
    """
    User model.

    :ivar first_name: first name customer.
    :vartype first_name: str
    :ivar last_name: last name customer.
    :vartype last_name: str
    :ivar email: email customer.
    :vartype email: str
    :ivar contact: contact customer.
    :vartype contact: str
    """

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    contact = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    description = models.TextField()

    projects = models.JSONField(blank=True, null=True)
    professions = models.JSONField(blank=True, null=True)
    hear_about_us = models.CharField(max_length=40)

def __str__(self):
    return self.first_name