from django.shortcuts import render, HttpResponse
def hello_world(request):
    return render(request, 'templates/hello_world.html')