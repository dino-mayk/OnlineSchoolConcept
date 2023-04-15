from django.shortcuts import render
from courses.models import Course


def list(request):
    template = 'courses/list.html'

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, template, context)
