from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.detail, name='article-detail'),
    path('logo/<str:symbol>', views.logo_image, name='company-logo'),
]
