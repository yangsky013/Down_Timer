import os
from pathlib import Path
import environ
from pymongo import MongoClient
import datetime


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
    'timer_name': '테스트 타이머2',
    "ready_min" : "03",
    "ready_sec" : "05",
    "exercise_min" : "02",
    "exercise_sec" : "10",
    "rest_min" : "02",
    "rest_sec" : "25",
    "round_count" : "01",
    "cycle_count" : "01",
    "between_cycle_min" : "01",
    "between_cycle_sec" : "30",
    "created_at": datetime.datetime.now(),
    "updated_at": datetime.datetime.now(),
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