from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.
def fbs(request):
    return HttpResponse('Function Based View')


class cbs(View):
    def get(self,request):
        return HttpResponse('Class Based String')
    
def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data inserted successfully...!')
    return render(request,'fbv_form.html',d)

class cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        
    # def post(self,request):
    #     if request.method=='POST':
    #         TFD=TopicForm(request.POST)
    #         if TFD.is_valid():
    #             TFD.save()
        return render(request,'cbv_form.html',d)