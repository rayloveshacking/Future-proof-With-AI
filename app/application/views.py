from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from django.shortcuts import redirect


def results(request):
    template = loader.get_template('results.html')
    return HttpResponse(template.render())

def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        role = request.POST['role']
        context = {'file': file, 'role': role}
        return redirect('results')
    else:
        template = loader.get_template('upload.html')
        return HttpResponse(template.render())
