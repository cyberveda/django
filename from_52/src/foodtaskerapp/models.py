from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from log import setup_logger

logger = setup_logger()


def upload_location_restaurant(instance, filename, **kwargs):
    file_path = 'restaurant/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class Restaurant(models.Model):
    # author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='restaurant')
    # name = models.CharField(max_length=500)
    title = models.CharField(max_length=50, null=False, blank=False)
    # phone = models.CharField(max_length=500)
    phone = models.CharField(max_length=50, null=False, blank=False)
    # address = models.CharField(max_length=500)
    address = models.CharField(max_length=50, null=False, blank=False)
    # logo = models.ImageField(upload_to='restaurant_logo/', blank=False)
    image = models.ImageField(upload_to=upload_location_restaurant, null=False, blank=False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'image'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Restaurant)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


# def pre_save_restaurant_receiever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.author.username + "-" + instance.title)


# pre_save.connect(pre_save_restaurant_receiever, sender=Restaurant)


class Customer(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.author.email

    class Meta:
        verbose_name = "App User Customer"
        verbose_name_plural = "App User Customers"


class Driver(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver')

    avatar = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.author.email

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


def upload_location_meal(instance, filename, **kwargs):
    file_path = 'meal/{name}-{filename}'.format(
        name=str(instance.name), filename=filename
    )
    return file_path


class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=upload_location_meal, null=False, blank=False)
    price = models.IntegerField(default=0)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 1 (Optional)")
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 2 (Optional)")
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 3 (Optional)")
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 4 (Optional)")
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 5 (Optional)")
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 6 (Optional)")
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 7 (Optional)")
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 8 (Optional)")
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 9 (Optional)")
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Photo 10 (Optional)")

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'image'

    def photo_1_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_1.url))

    photo_1_tag.short_description = 'photo_1'

    def photo_2_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_2.url))

    photo_2_tag.short_description = 'photo_2'

    def photo_3_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_3.url))

    photo_3_tag.short_description = 'photo_3'

    def photo_4_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_4.url))

    photo_4_tag.short_description = 'photo_4'

    def photo_5_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_5.url))

    photo_5_tag.short_description = 'photo_5'

    def photo_6_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_6.url))

    photo_6_tag.short_description = 'photo_6'

    def photo_7_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_7.url))

    photo_7_tag.short_description = 'photo_7'

    def photo_8_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_8.url))

    photo_8_tag.short_description = 'photo_8'

    def photo_9_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_9.url))

    photo_9_tag.short_description = 'photo_9'

    def photo_10_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_10.url))

    photo_10_tag.short_description = 'photo_10'

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name


class Order(models.Model):
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES = (
        (COOKING, "Cooking"),
        (READY, "Ready"),
        (ONTHEWAY, "On the way"),
        (DELIVERED, "Delivered"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    picked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    class Meta:
        verbose_name = "Order Details"
        verbose_name_plural = "Order Details"

    def __str__(self):
        return str(self.id)
