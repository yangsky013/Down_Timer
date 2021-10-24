from django.shortcuts import render, redirect
from .models import Timer

# Create your views here.

def cycles(request):
    timers = Timer.objects.all()
    # for timer in timers:
    #     timer.exercise_list = [exercise['exercise_name'] for exercise in timer.exercise_list]
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

def post(request):
  if request.method == 'POST' and 'save' in request.POST:

    timer_name = request.POST['timer_name']
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
      'timer_name': timer_name,
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

    # TODO: Will be changed
    TimerData['created_at'] = datetime.datetime.now()
    TimerData['updated_at'] = datetime.datetime.now()

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

def update(request):
  if request.method == 'POST' and 'update' in request.POST:

    timer_name = request.POST['timer_name']
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
      'timer_name': timer_name,
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

    # TODO: Will be changed
    TimerData['created_at'] = datetime.datetime.now()
    TimerData['updated_at'] = datetime.datetime.now()

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

    timer.find_one({'timer_name': timer_name,})
    timer.update_one({'timer_name': timer_name,},
    { "$set" : TimerData})

    return redirect('cycles/')

  elif request.method == 'POST' and 'delete' in request.POST:

    timer_name = request.POST['timer_name']

    TimerData = {
      'timer_name': timer_name,
    }
    import os
    from pathlib import Path
    import environ
    import datetime
    from pymongo import MongoClient

    # TODO: Will be changed
    TimerData['created_at'] = datetime.datetime.now()
    TimerData['updated_at'] = datetime.datetime.now()

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

    timer.delete_one({'timer_name': timer_name,})

    return redirect('cycles/')