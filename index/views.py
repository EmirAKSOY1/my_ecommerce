from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('../main_template/index/index.html')
    return HttpResponse(template.render())
