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

timer_sample = {
    'timer_name': '테스트 타이머',
    'exercise_list': ['푸시 업', '윗몸 일으키기'],
    'exercise_time': 100,
    'rest_time': 20,
    'time_between_cycle': 10,
    'ready_time': 10,
    'cycle_count': 3,
    'round_count': 5,
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now(),
}
timer.insert_one(timer_sample)
print('test complete')

'''
schema)
    _id = models.ObjectIdField(auto_created=True, unique=True, primary_key=True)
    timer_name = models.CharField(max_length=255)
    exercise_list = models.EmbeddedField(model_container=Exercise)
    exercise_time = models.IntegerField()
    rest_time = models.IntegerField()
    time_between_cycle = models.IntegerField()
    ready_time = models.IntegerField()
    cycle_count = models.IntegerField()
    round_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
'''