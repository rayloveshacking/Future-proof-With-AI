from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def upload(request):
    template = loader.get_template('upload.html')
    return HttpResponse(template.render())