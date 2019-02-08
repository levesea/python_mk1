from django.conf.urls import include,url
import app.views

urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^home$', app.views.index, name='home'),
    url(r'about$', app.views.about, name='about'),
]