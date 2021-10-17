from django.shortcuts import render, redirect
from .models import Timer

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

def post(request):
  if request.method == 'POST':
    
    print(request)

    exercise_name = request.POST['exercise_name']
    ready_min = request.POST['ready_min']
    ready_sec = request.POST['ready_sec']
    exercise_min = request.POST['exercise_min']
    exercise_sec = request.POST['exercise_sec']
    rest_min = request.POST['rest_min']
    rest_sec = request.POST['rest_sec']
    round_count = request.POST['round_count']
    cycle_count = request.POST['cycle_count']
    between_cycle_min = request.POST['between_cycle_min']
    between_cycle_sec = request.POST['between_cycle_sec']

    TimerData = {
      'exercise_name': exercise_name,
      'ready_min': ready_min,
      'ready_sec' : ready_sec,
      'exercise_min' : exercise_min,
      'exercise_sec' : exercise_sec,
      'rest_min' : rest_min,
      'rest_sec' : rest_sec,
      'round_count' : round_count,
      'cycle_count' : cycle_count,
      'between_cycle_min' : between_cycle_min,
      'between_cycle_sec' : between_cycle_sec,
    }
    import os
    from pathlib import Path
    import environ
    import datetime
    from pymongo import MongoClient

    BASE_DIR = Path(__file__).resolve().parent
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    host = env('DB_HOST')
    port = int(env('DB_PORT'))
    username = env('DB_USERNAME')
    password = env('DB_PASSWORD')

    client = MongoClient(host=host,
                        port=int(port),
                        username=username,
                        password=password
                        )
    db = client['down-timer']
    timer = db['timer']

    timer.insert_one(TimerData)

    return redirect('cycles/')