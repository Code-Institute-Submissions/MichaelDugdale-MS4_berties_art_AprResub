from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('return-policy/', views.return_policy, name='return_policy'),
    path('faq/', views.faq, name='faq'),
]
