from django.http import HttpResponse
import json
 
from timer.MongoDbManager import MongoDbManager
 
def specific_user(request, username):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({'name': username})
        responseData = dbUserData[0]
        del responseData['_id']
 
        return HttpResponse(json.dumps(responseData), status=200)
 
    def post():
        try:
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

        except:
            return HttpResponse(status=400)
 
        userData = {
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
 
        result = MongoDbManager().add_user_on_collection(userData)
        return HttpResponse(status=201) if result else HttpResponse(status=500)
 
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse(status=405)
 
def all_users( request):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({})
        responseData = []
        for user in dbUserData:
            del user['_id']
            responseData.append(user)
 
        return HttpResponse(json.dumps(responseData), status=200)
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)