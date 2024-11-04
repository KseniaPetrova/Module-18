from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def classTemplate(request):
    return render(request, "second_task/class_template.html")

class funcTemplate(TemplateView):
    template_name = 'second_task/func_template.html'
