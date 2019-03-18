"""petHelperApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name = 'index'),

    url(r'^contact$', views.contact, name = 'contact'),

    url(r'^legal_information$', views.legal_information, name = 'legal_information'),

    url(r'^about$', views.about, name = 'about'), 
      
    url(r'^help/$', views.help, name = 'help'),
      
    url(r'^signup/$', views.signup, name = 'signup'),

    url('accounts/', include('django.contrib.auth.urls')),

    url(r'^courses/$', views.courses, name = 'courses'),

    url(r'^profile/$', views.profile, name='profile'),

    url(r'^suggestions/$', views.suggestions, name='suggestions'),

    url(r'all_suggestions/$', views.all_suggestions, name='all_suggestions'),

    url(r'suggestions/delete/(?P<id>\d+)$', views.delete_suggestion, name='delete_suggestion'),

    url(r'^internships/$', views.internships, name='internships'),

    url(r'all_internships/$', views.all_internships, name='all_internships'),

    url(r'internships/delete/(?P<id>\d+)$', views.delete_internship, name='delete_internships'),

    url(r'^jobs/$', views.jobs, name='jobs'),

    url(r'all_jobs/$', views.all_jobs, name='all_jobs'),

    url(r'jobs/delete/(?P<id>\d+)$', views.delete_job, name='delete_job'),
]
