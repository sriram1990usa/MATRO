from django.urls import include, path
from paytm import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),
]
