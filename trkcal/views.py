from django.shortcuts import render
from django.utils import timezone
from .models import Recurring, Daily, Due 

def main_display(request):
    recurringtasks = Recurring.objects.all()
    dailytasks = Daily.objects.all()
    duetasks = Due.objects.all()
    return render(request, 'trkcal/index.html', {'recurringtasks' : recurringtasks,
                                                 'dailytasks' : dailytasks,
                                                 'duetasks' : duetasks,})

