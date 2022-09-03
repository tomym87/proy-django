from itertools import count
from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, unique=False)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    tagone = models.CharField(max_length=100, unique=False, default='PE4710')
    col = models.CharField(max_length=100, unique=False, default='bg-primary')
    prod_catalogo = models.CharField(max_length=100, unique=False, default='https://valtic.com.mx')
    prod_pre = models.CharField(max_length=100, unique=False, default='https://valtic.com.mx')
    prod_fich = models.CharField(max_length=100, unique=False, default='https://valtic.com.mx')
    e4 = models.CharField(max_length=100, unique=False, default='https://valtic.com.mx')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_min = models.BooleanField(default=True)
    is_indu = models.BooleanField(default=True)
    is_oil = models.BooleanField(default=True)
    is_ener = models.BooleanField(default=True)
    is_apot = models.BooleanField(default=True)
    is_ares = models.BooleanField(default=True)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class VariationManager(models.Manager):
    def rds(self):
        return super(VariationManager, self).filter(variation_category='rd', is_active=True)
    def diametros(self):
        return super(VariationManager, self).filter(variation_category='diametro', is_active=True)

variation_category_choice = (
    ('diametro', 'diametro'),
    ('rd', 'rd'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_category + ':' + self.variation_value

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.CharField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.subject
    
variation_uso_choice=(
    ('mineria', 'Mineria'),
    ('industrial', 'Industrial'),
    ('oil y gas', 'OPil y Gas'),
    ('energia', 'Energia'),
    ('agua potable', 'Agua potable'),
    ('agua residual', 'Agua Residual'),
    
)
    

     
