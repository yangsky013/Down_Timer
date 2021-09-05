from djongo import models


# Create your models here.
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Timer(models.Model):
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

    class Meta:
        db_table = 'timer'
