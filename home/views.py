from django.shortcuts import render
from .models import Person

def hello_world(request):
    people = Person.objects.all()
    context = {
        'people': people
    }
    return render(request, 'index.html', context)
