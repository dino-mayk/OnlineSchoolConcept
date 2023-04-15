from django.contrib import admin

from tutors.models import Tutor


@admin.register(Tutor)
class AdminTutor(admin.ModelAdmin):
    list_display = [
        'title',
    ]
