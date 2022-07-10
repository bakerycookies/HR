from django.shortcuts import render

# Function to render Homepage
def home(request):
    return render(request, "home.html")