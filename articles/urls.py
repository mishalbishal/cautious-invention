from django.urls import path

from . import views

urlpatterns = [
    path('logo/<str:symbol>', views.logo_image, name='company-logo'),
    path('author/<int:author_id>', views.hotlink_author_profile, name='author-hotlink'),
    path('article/<slug:slug>', views.detail, name='article-detail'),
]
