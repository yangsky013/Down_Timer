from django.shortcuts import render, redirect
from .models import Timer
import json
from bson.json_util import loads, dumps
from bson import ObjectId

# Create your views here.

def cycles(request):
    timers = Timer.objects.all()
    total_timer_count = len(timers)
    inactive_timer_count = len([timer.is_active for timer in timers if timer.is_active == 'false'])
    if total_timer_count - inactive_timer_count  != 1:
        for timer in timers:
            timer.is_active = 'false'
        timers[0].is_active = 'true'
    timers_js = json.dumps([timer for timer in Timer.objects.values()], default=str)
    context = {
        'timers': timers,
        'timers_js': timers_js,
    }
    return render(request, 'cycles.html', context=context)

def test(request):
  timers = Timer.objects.all()
  # for timer in timers:
  #     timer.exercise_list = [exercise['exercise_name'] for exercise in timer.exercise_list]
  
  for timer in timers:
    if timer.is_active == 'true':
      def_time = timer

  tmp = int(def_time.ready_min) * 60 + int(def_time.ready_sec)
  for i in range(int(def_time.cycle_count)):
    for j in range(int(def_time.round_count)):
      tmp += int(def_time.exercise_min) * 60 + int(def_time.exercise_sec)
      if j < int(def_time.round_count) - 1:
        tmp += int(def_time.rest_min) * 60 + int(def_time.rest_sec)
    if i < int(def_time.cycle_count) - 1:
      tmp += int(def_time.between_cycle_min) * 60 + int(def_time.between_cycle_sec)
  def_time.total_min = tmp // 60
  def_time.total_sec = tmp % 60

  context = {
      'timers': timers,
      'def_time' : def_time,
  }
  return render(request,'timer/index.html', context=context)

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
      'is_active' : 'false'
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

    timer_id = request.POST['timer_id']
    print('timer_id', timer_id)
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

    # timer.find_one({'timer_name': timer_name,})
    # timer.update_one({'timer_name': timer_name,},
    # { "$set" : TimerData})

    timer.find_one({'_id': ObjectId(timer_id)})
    timer.update_one({'_id': ObjectId(timer_id)}, { "$set" : TimerData})

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

  
def select(request):
  if request.method == 'POST' and 'select' in request.POST:
    timer_id = request.POST['timer_id']
    print('timer_id', timer_id)

    import os
    from pathlib import Path
    import environ
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

    print(timer.find_one({'_id': ObjectId(timer_id)}))
    timer.update_many({}, {"$set": {'is_active': "false"}})
    timer.update_one({'_id': ObjectId(timer_id)}, { "$set" : {'is_active': "true"}})
    return redirect('/')