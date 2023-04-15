from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = [
        'title',
    ]
