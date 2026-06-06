from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('product-details/<pk>/<file_name>', views.product_details, name='product_details'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
