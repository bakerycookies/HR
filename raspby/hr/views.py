from django.shortcuts import render

def fronted(request):
    return render(request, "frontend.html")

def backend(request):
    return render(request, "backend.html")


