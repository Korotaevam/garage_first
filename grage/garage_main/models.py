from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class AutoModels(models.Model):
    articles = models.CharField(max_length=255, blank=True, verbose_name='Articles')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    group = models.CharField(max_length=255, blank=True)
    subgroup = models.CharField(max_length=255, blank=True)
    vendor = models.CharField(max_length=255, blank=True)
    vendor_code = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    auto_model = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    margin = models.FloatField(default=1, validators=[MinValueValidator(0)])
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    content_extra = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    group_add = models.ForeignKey('GroupAdd', on_delete=models.PROTECT, null=True)
    sub_group_add = models.ForeignKey('SubGroupAdd', on_delete=models.PROTECT, null=True)
    model_add = models.ForeignKey('ModelAdd', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return ' '.join(map(str, [self.brand, self.group, self.subgroup]))

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'
        ordering = ['id']


class GroupAdd(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)

    def __str__(self):
        return self.name


class SubGroupAdd(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)

    def __str__(self):
        return self.name


class ModelAdd(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_models', kwargs={'model_add_id_1': self.pk})
