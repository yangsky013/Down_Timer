from django.shortcuts import render
from .models import Timer

# Create your views here.

def cycles(request):
    timers = Timer.objects.all()
    for timer in timers:
        timer.exercise_list = [exercise['exercise_name'] for exercise in timer.exercise_list]
    context = {
        'timers': timers,
    }
    return render(request, 'cycles.html', context=context)

def test(request):
  return render(request,'timer/index.html')

def write(request):
  return render(request,'write.html')
  
def edit(request):
  return render(request,'edit.html')

def settings(request):
    return render(request,'timer/settings.html')