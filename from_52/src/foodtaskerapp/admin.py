# from django.contrib import admin
#
# from .models import Restaurant, Customer, Meal, Order, OrderDetails, Driver
#
# admin.site.register(Driver)
#
#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'author', 'author_id', 'phone', 'address', 'avatar')
#     search_fields = ('pk', 'author', 'phone')
#     readonly_fields = ('pk',)
#     list_display_links = ('pk', 'author')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'customer', 'restaurant', 'address', 'total', 'status', 'created_at', 'picked_at')
#     search_fields = ('pk', 'customer', 'restaurant')
#     readonly_fields = ('pk', 'created_at', 'picked_at')
#     list_display_links = ('pk', 'customer', 'restaurant')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# class OrderDetailsAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'order', 'meal', 'quantity', 'sub_total')
#     search_fields = ('pk', 'order', 'meal')
#     readonly_fields = ('pk',)
#     list_display_links = ('pk', 'order')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'author', 'phone', 'address', 'image_tag')
#     search_fields = ('pk', 'title', 'author')
#     readonly_fields = ('pk', 'image_tag')
#     list_display_links = ('pk', 'title')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#     fields = ('pk', 'author', 'title', 'phone', 'address', 'image', 'image_tag')
#
#
# class MealAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk', 'restaurant', 'name', 'short_description', 'price', 'image_tag')
#     search_fields = ('pk', 'restaurant', 'name')
#     readonly_fields = (
#         'pk', 'image_tag', 'photo_1_tag', 'photo_2_tag', 'photo_3_tag', 'photo_4_tag', 'photo_5_tag', 'photo_6_tag',
#         'photo_7_tag', 'photo_8_tag', 'photo_9_tag', 'photo_10_tag')
#     list_display_links = ('pk', 'restaurant', 'name')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#     fields = (
#         'pk', 'restaurant', 'name', 'short_description', 'price', 'image', 'image_tag', 'photo_1', 'photo_1_tag',
#         'photo_2', 'photo_2_tag', 'photo_3', 'photo_3_tag', 'photo_4', 'photo_4_tag', 'photo_5', 'photo_5_tag',
#         'photo_6', 'photo_6_tag', 'photo_7', 'photo_7_tag', 'photo_8', 'photo_8_tag', 'photo_9', 'photo_9_tag',
#         'photo_10', 'photo_10_tag')
#
#
# # admin.site.register(Restaurant, RestaurantAdmin)
# # admin.site.register(Customer, CustomerAdmin)
# # admin.site.register(Meal, MealAdmin)
# # admin.site.register(Order, OrderAdmin)
# # admin.site.register(OrderDetails, OrderDetailsAdmin)
