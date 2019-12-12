from django.http import HttpResponse
from django.shortcuts import render
from django_resume.handlers.resume_data import ResumeData

# Create your views here.
def index(request):
    data = ResumeData().get_resume_data()
    context = {'resume_data': data}
    return render(request, 'django_resume/index.html', context)

def health(request):
    return HttpResponse('OK')