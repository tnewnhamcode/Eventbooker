from django.contrib import admin
from django.urls import path, include
from posts import views as posts_urls
from django.views.generic import TemplateView
from user import views
from user import urls as user_urls
from django.urls import reverse

urlpatterns = [
    path('', TemplateView.as_view(template_name='posts/home.html'), name='home'),
    path('logout1', include(user_urls)),
    path ('Funtime Disco/', TemplateView.as_view(template_name='posts/Funtime Disco.html'), name='Funtime Disco'),
    path ('Funtime Disco/payscreen/', posts_urls.payscreen, name='payscreen'),
    path ('Funtime Disco/payscreen/successcreen', TemplateView.as_view(template_name='successcreen.html'), name='successcreen'),
    path ('Badass TEchno eXremity/', TemplateView.as_view(template_name='posts/Badass TEchno eXremity.html'), name='Badass TEchno eXtremity'),
    path ('Badass TEchno eXremity/payscreen/', posts_urls.payscreen, name='payscreen'),
    path ('Badass TEchno eXremity/payscreen/successcreen', TemplateView.as_view(template_name='successcreen.html'), name='successcreen'),
    path ("Love and that's all/", TemplateView.as_view(template_name="posts/Love and that's all.html"), name='love and that&#39;s all'),
     path ("Love and that's all/payscreen/", posts_urls.payscreen, name='payscreen'),
    path ("Love and that's all/payscreen/successcreen", TemplateView.as_view(template_name='successcreen.html'), name='successcreen'),
    path ("Bowling Bonanza/", TemplateView.as_view(template_name="posts/Bowling Bonanza.html"), name='Bowling Bonanza'),
]
