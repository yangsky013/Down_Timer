from django.shortcuts import render

# Create your views here.

def cycles(request):
    return render(request, 'cycles.html')


def test(request):
  return render(request,'timer/index.html')