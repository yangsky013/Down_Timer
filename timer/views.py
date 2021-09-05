from django.shortcuts import render

# Create your views here.

def cycles(request):
    return render(request, 'cycles.html')

def test(request):
  return render(request,'timer/index.html')

def write(request):
  return render(request,'write.html')
  
def edit(request):
  return render(request,'edit.html')

def settings(request):
    return render(request,'timer/settings.html')