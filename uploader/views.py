from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Files
from .forms import FilesForm
import mimetypes
import os
# Create your views here.

def files(request):
    return render(request, 'files.html')

# fungsi untuk hasil form (details)
def postform(request):
    files = Files.objects.all()
    response = {
        'files' : files
    }
    return render(request, 'postform.html', response)

# fungsi untuk form
def preform(request):
    regist = FilesForm()
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()

        return HttpResponseRedirect('/postform')

    response = {
        'regist' : regist
    }

    return render(request, 'preform.html', response)


def download(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/documents/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponseRedirect(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'files.html')