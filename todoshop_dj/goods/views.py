from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View


class Index(View):
    def get(self,request):
        return JsonResponse({"code":200})
    def post(self,request):
        pass