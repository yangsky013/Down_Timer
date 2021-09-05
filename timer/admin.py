from django.contrib import admin
from .models import Timer

# Register your models here.
admin.register(Timer) # admin.site.register(Timer) does not work