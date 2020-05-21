from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects.all()
    
    return render(request, 'jobs/home.html', {'jobs': jobs})



def blog(request):
    pass

def resume(request):
    pass
