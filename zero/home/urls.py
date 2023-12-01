from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home,name='home'),
    path('signup', views.handleSignup,name='handleSignup'),
    path('abc', views.branch,name='branch'),
    path('login', views.handleLogin,name='handleLogin'),
    path('logout', views.handleLogout,name='handleLogout'),
    path('efg', views.bye,name='bye'),
    # path('upload', views.upload,name='upload'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#ravi-sunny0821