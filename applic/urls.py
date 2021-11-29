from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog.html'), name='index'),
    path('rsa', views.rsa_view, name='rsa'),
    path('elgamal', views.elgamal_view, name='elgamal'),
    path('rabin', views.rabin_view, name='rabin'),
    path('send', views.send),
    path('rsasend', views.rsasend),
    path('rsasign', views.rsasign),
    path('rabinsend', views.rabinsend),
]
