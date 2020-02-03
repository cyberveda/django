from django.contrib import admin

from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'author', 'date_published', 'date_updated', 'slug', 'image_tag')
    search_fields = ('pk', 'title', 'author__username', 'slug')
    readonly_fields = (
        'pk', 'image_tag', 'photo_1_tag', 'photo_2_tag', 'photo_3_tag', 'photo_4_tag', 'photo_5_tag', 'photo_6_tag',
        'photo_7_tag', 'photo_8_tag', 'photo_9_tag', 'photo_10_tag', 'photo_11_tag', 'photo_12_tag', 'photo_13_tag',
        'photo_14_tag', 'photo_15_tag', 'photo_16_tag',
        'photo_17_tag', 'photo_18_tag', 'photo_19_tag', 'photo_20_tag', 'photo_21_tag', 'photo_22_tag', 'photo_23_tag',
        'photo_24_tag', 'photo_25_tag', 'photo_26_tag',
        'photo_27_tag', 'photo_28_tag', 'photo_29_tag', 'date_published', 'date_updated', 'slug')
    list_display_links = ('pk', 'title', 'slug')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    fields = (
        'pk', 'title', 'author', 'body', 'date_published', 'date_updated', 'slug', 'image', 'image_tag', 'photo_1',
        'photo_1_tag',
        'photo_2', 'photo_2_tag', 'photo_3', 'photo_3_tag', 'photo_4', 'photo_4_tag', 'photo_5', 'photo_5_tag',
        'photo_6', 'photo_6_tag', 'photo_7', 'photo_7_tag', 'photo_8', 'photo_8_tag', 'photo_9', 'photo_9_tag',
        'photo_10', 'photo_10_tag', 'photo_11',
        'photo_11_tag',
        'photo_12', 'photo_12_tag', 'photo_13', 'photo_13_tag', 'photo_14', 'photo_14_tag', 'photo_15', 'photo_15_tag',
        'photo_16', 'photo_16_tag', 'photo_17', 'photo_17_tag', 'photo_18', 'photo_18_tag', 'photo_19', 'photo_19_tag',
        'photo_20', 'photo_20_tag', 'photo_21',
        'photo_21_tag',
        'photo_22', 'photo_22_tag', 'photo_23', 'photo_23_tag', 'photo_24', 'photo_24_tag', 'photo_25', 'photo_25_tag',
        'photo_26', 'photo_26_tag', 'photo_27', 'photo_27_tag', 'photo_28', 'photo_28_tag', 'photo_29', 'photo_29_tag',)


admin.site.register(BlogPost, BlogPostAdmin)
