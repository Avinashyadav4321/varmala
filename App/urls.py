from django.urls import path
from . import views


urlpatterns = [
    path('',views.Homepage ,name='home'),
    path('about/',views.About ,name='about'),
    path('services/',views.Services ,name='services'),
    path('why-choose-us/',views.Why_Choose_Us ,name='why_choose'),
    path('pricing/',views.Pricing ,name='pricing'),
    path('gallery/',views.Gallery ,name='gallery'),
    path('blogs/',views.Blog ,name='blog'),
    path('thanks/',views.Thanks ,name='thanks'),
    path('contact/',views.Contact ,name='contact'),
]
