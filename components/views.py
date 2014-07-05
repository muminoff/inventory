from django.shortcuts import render
from components.models import Component
from datetime import datetime


def components_page(request):
    context = {
        'components': Component.objects.all(),
        'time': datetime.now()
    }
    return render(request, 'components.html', context)
