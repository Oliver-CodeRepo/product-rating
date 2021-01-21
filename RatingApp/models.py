from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField, SlugField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORY_CHOICES = (
    ('Technical', 'Technical'),
    ('Consumable','Consumable'),
    ('Sports','Sports'),
    ('Fashion','Fashion')
)

class Product(models.Model):
    slug = models.SlugField()
    p_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse('product-details', kwargs={'p_slug':self.slug})

    @property
    def productReview(self):
        return self.review_set.all()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=50)
    user_email = models.EmailField()
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'On {}, By {}'.format(str(self.product), self.user)

    def get_absolute_url(self):
        return reverse('product-details')