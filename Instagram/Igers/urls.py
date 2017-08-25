from django.conf.urls import url, include
from Igers import views

urlpatterns = [
    url(r'^login', views.UserCreateView.as_view(), name='login'),
]