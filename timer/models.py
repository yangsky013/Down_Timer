from djongo import models
from django import forms


# Create your models here.
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        managed = False

    def __str__(self):
        return self.exercise_name

class Timer(models.Model):
    _id = models.ObjectIdField(auto_created=True, unique=True, primary_key=True)
    timer_name = models.CharField(max_length=255)
    exercise_list = models.ArrayField(model_container=Exercise)
    exercise_time = models.IntegerField()
    rest_time = models.IntegerField()
    time_between_cycle = models.IntegerField()
    ready_time = models.IntegerField()
    cycle_count = models.IntegerField()
    round_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'timer'
