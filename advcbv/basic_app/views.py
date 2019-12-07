from django.shortcuts import render
from django.views.generic import View,TemplateView

#from django.http import HttpResponse
# Create your views here.

#function based view
'''
def index(request):
    return render(request,'index.html')
'''

# Class Based View Example
'''
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based View (CBV) are so COOL!")
'''

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic Injection example!'
        return context 
