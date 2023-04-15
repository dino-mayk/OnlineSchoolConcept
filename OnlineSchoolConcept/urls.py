from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls'), name='grappelli'),

    path('', include('homepage.urls'), name='homepage'),
    path('about/', include('about.urls'), name='about'),
    path('courses/', include('courses.urls'), name='courses'),
    path('tutors/', include('tutors.urls'), name='tutors'),
]
