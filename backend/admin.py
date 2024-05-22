from django.contrib import admin

# Register your models here.

 # Import the Event model from the current app's models
from .models import Event 
# Register the Event model with the admin interface
admin.site.register(Event)  
