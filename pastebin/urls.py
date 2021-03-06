from django.contrib import admin
from django.conf.urls import url, include
from posts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.create, name="home"),
]

urlpatterns += staticfiles_urlpatterns()