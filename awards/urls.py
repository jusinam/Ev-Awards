from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home, name= 'home'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),


]
