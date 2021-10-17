from djongo import models


# Create your models here.
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Timer(models.Model):
    _id = models.ObjectIdField(auto_created=True, unique=True, primary_key=True)
    # timer_name = models.CharField(max_length=255)
    # exercise_list = models.EmbeddedField(model_container=Exercise)
    # exercise_time = models.IntegerField()
    # rest_time = models.IntegerField()
    # time_between_cycle = models.IntegerField()
    # ready_time = models.IntegerField()
    # cycle_count = models.IntegerField()
    # round_count = models.IntegerField()
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    exercise_name = models.CharField(max_length=255)
    ready_min = models.IntegerField()
    ready_sec = models.IntegerField()
    exercise_min = models.IntegerField()
    exercise_sec = models.IntegerField()
    rest_min = models.IntegerField()
    rest_sec = models.IntegerField()
    round_count = models.IntegerField()
    cycle_count = models.IntegerField()
    between_cycle_min = models.IntegerField()
    between_cycle_sec = models.IntegerField()

    class Meta:
        db_table = 'timer'
