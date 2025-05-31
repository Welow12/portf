from django.shortcuts import render
from django.http import HttpResponse
import mimetypes

# Create your views here.

def Home(request):
    return render(request, 'Base/home.html')

def About(request):
    return render(request, 'Base/about.html')

def Portfolio(request):
    return render(request, 'Base/portfolio.html')

def Contact(request):
    return render(request, 'Base/contact.html')

def Resume(request):
    return render(request, 'Base/resume.html')

def Services(request):
    return render(request, 'Base/services.html')

def Testimony(request):
    return render(request, 'Base/testimony.html')

def Portfolio_details(request):
    return render(request, 'Base/portfolio-details.html')

def Confirmation(request):
    return render(request, 'Base/confirmation.html')

def Service_details(request):
    return render(request, 'Base/service-details.html')

def Download_file(request):
    # fill these variables with real values
    fl_path = 'C:\\Users\\bruno\\Desktop\\Eccomerce\\Base\\static\\BRUNO CV.pdf'
    filename = 'BRUNO CV.pdf'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response