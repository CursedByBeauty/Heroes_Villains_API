from django.urls import path
from . import views

urlpatterns = [
    path("", views.super_types_list),
    # path("<pk>/", views.super_types_detail),
]

# urlpatterns = [
#      path("super_types/", views.super_types_list),
# ]