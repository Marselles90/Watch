from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.product_view, name='product'),
    path('watch/<int:watch_id>/', views.watch_detail, name='watch_detail'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
]