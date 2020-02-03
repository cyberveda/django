from django.urls import path
from about.api.views import (
    api_detail_about_view,
    api_update_about_view,
    api_delete_about_view,
    api_create_about_view,

    ApiAboutListView,
    api_is_author_of_aboutpost)

app_name = 'about'

urlpatterns = [
    path('<slug>/', api_detail_about_view, name="detail"),
    path('<slug>/update', api_update_about_view, name="update"),
    path('<slug>/delete', api_delete_about_view, name="delete"),
    path('create', api_create_about_view, name="create"),
    path('list', ApiAboutListView.as_view(), name="list"),
    path('<slug>/is_author', api_is_author_of_aboutpost, name="is_author"),
]
