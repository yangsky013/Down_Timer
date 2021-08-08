from django.shortcuts import render

# Create your views here.

def cycles(request):
    return render(request, 'cycles.html')

def test(request):
  return render(request,'timer/index.html')

def views(request):
  return render(request,'view.html')

def settings(request):
    return render(request,'timer/settings.html')