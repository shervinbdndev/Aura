from django.shortcuts import render
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from utils.error import Errors
from utils.server_side_data import data





class Error400View(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            template_name='error/error.html',
            status=400,
            context={
                'server': data,
                'err_code': Errors.E_400,
                'err_desc': Errors.E_400_DESC,
            }
        )
        
        
        
        
        
class Error403View(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            template_name='error/error.html',
            status=403,
            context={
                'server': data,
                'err_code': Errors.E_403,
                'err_desc': Errors.E_403_DESC,
            }
        )
        
        
        
        
        
        
class Error404View(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            template_name='error/error.html',
            status=404,
            context={
                'server': data,
                'err_code': Errors.E_404,
                'err_desc': Errors.E_404_DESC,
            }
        )
        
        
        
        
        
class Error500View(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(
            request=request,
            template_name='error/error.html',
            status=500,
            context={
                'server': data,
                'err_code': Errors.E_500,
                'err_desc': Errors.E_500_DESC,
            }
        )