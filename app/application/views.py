from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.conf import settings

def results(request):
    file_path = request.session.get('file_path')
    role = request.session.get('role')
    context = {'file_path': file_path, 'role': role}
    template = loader.get_template('results.html')
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        role = request.POST['role']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        default_storage.save(file_path, file)
        request.session['file_path'] = file_path
        request.session['role'] = role
        return redirect('results')
    else:
        template = loader.get_template('upload.html')
        return HttpResponse(template.render({}, request)) # correct render.

def talent(request):
    template = loader.get_template('talent.html')
    return HttpResponse(template.render({}, request))

