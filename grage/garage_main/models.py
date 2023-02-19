from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class AutoModels(models.Model):
    articles = models.CharField(max_length=255, blank=True)
    group = models.CharField(max_length=255, blank=True)
    subgroup = models.CharField(max_length=255, blank=True)
    vendor = models.CharField(max_length=255,blank=True)
    vendor_code = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    auto_model = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    content_extra = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return ' '.join(map(str, [self.articles, self.group, self.subgroup]))

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_id': self.pk})
