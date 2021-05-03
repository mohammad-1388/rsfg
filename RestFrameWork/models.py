from django.db import models
from datetime import datetime


class Book(models.Model):
    """
    The Model Represent a Book
    """
    name = models.CharField('name', max_length=255)
    store_name = models.CharField('Store', max_length=255)
    description = models.TextField('Description')
    image = models.ImageField(verbose_name='Image', default='', upload_to='store_image/', null=True, blank=True)
    fav = models.BooleanField(verbose_name='Fav', default=False)
    create_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name + " - " + self.store_name
