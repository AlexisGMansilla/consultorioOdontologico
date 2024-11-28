from django.shortcuts import render
from datetime import datetime

def home(request):
    today = datetime.now()
    return render(request, 'home.html', {
        'year': today.year,
        'month': today.month,
    })
