from django.shortcuts import render
from django.http import HttpResponse

def pagina1(request):
    return HttpResponse(f"{request.user}")

def pagina2(request):
    return render(request,'home.html')