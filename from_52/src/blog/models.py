from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe


def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    body = models.TextField(max_length=5000, null=False, blank=True)
    image = models.ImageField(upload_to=upload_location, null=False, blank=True, default='ww.png')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    photo_1 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 1 (Optional)")
    photo_2 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 2 (Optional)")
    photo_3 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 3 (Optional)")
    photo_4 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 4 (Optional)")
    photo_5 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 5 (Optional)")
    photo_6 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 6 (Optional)")
    photo_7 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 7 (Optional)")
    photo_8 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 8 (Optional)")
    photo_9 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 9 (Optional)")
    photo_10 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 10 (Optional)")

    photo_11 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 11 (Optional)")
    photo_12 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 12 (Optional)")
    photo_13 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 13 (Optional)")
    photo_14 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 14 (Optional)")
    photo_15 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 15 (Optional)")
    photo_16 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 16 (Optional)")
    photo_17 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 17 (Optional)")
    photo_18 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 18 (Optional)")
    photo_19 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 19 (Optional)")
    photo_20 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 20 (Optional)")

    photo_21 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 21 (Optional)")
    photo_22 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 22 (Optional)")
    photo_23 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 23 (Optional)")
    photo_24 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 24 (Optional)")
    photo_25 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 25 (Optional)")
    photo_26 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 26 (Optional)")
    photo_27 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 27 (Optional)")
    photo_28 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 28 (Optional)")
    photo_29 = models.ImageField(upload_to=upload_location, blank=True, verbose_name="Photo 29 (Optional)")

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

    def photo_11_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_11.url))

    photo_11_tag.short_description = 'photo_11'

    def photo_12_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_12.url))

    photo_12_tag.short_description = 'photo_12'

    def photo_13_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_13.url))

    photo_13_tag.short_description = 'photo_13'

    def photo_14_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_14.url))

    photo_14_tag.short_description = 'photo_14'

    def photo_15_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_15.url))

    photo_15_tag.short_description = 'photo_15'

    def photo_16_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_16.url))

    photo_16_tag.short_description = 'photo_16'

    def photo_17_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_17.url))

    photo_17_tag.short_description = 'photo_17'

    def photo_18_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_18.url))

    photo_18_tag.short_description = 'photo_18'

    def photo_19_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_19.url))

    photo_19_tag.short_description = 'photo_19'

    def photo_20_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_20.url))

    photo_20_tag.short_description = 'photo_20'

    def photo_21_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_21.url))

    photo_21_tag.short_description = 'photo_21'

    def photo_22_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_22.url))

    photo_22_tag.short_description = 'photo_22'

    def photo_23_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_23.url))

    photo_23_tag.short_description = 'photo_23'

    def photo_24_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_24.url))

    photo_24_tag.short_description = 'photo_24'

    def photo_25_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_25.url))

    photo_25_tag.short_description = 'photo_25'

    def photo_26_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_26.url))

    photo_26_tag.short_description = 'photo_26'

    def photo_27_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_27.url))

    photo_27_tag.short_description = 'photo_27'

    def photo_28_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_28.url))

    photo_28_tag.short_description = 'photo_28'

    def photo_29_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo_29.url))

    photo_29_tag.short_description = 'photo_29'

    def __str__(self):
        return self.title


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiever, sender=BlogPost)
