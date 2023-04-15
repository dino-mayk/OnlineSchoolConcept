from django.shortcuts import render
from tutors.models import Tutor


def list(request):
    template = 'tutors/list.html'

    tutors = Tutor.objects.all()

    context = {
        'tutors': tutors,
    }

    return render(request, template, context)
