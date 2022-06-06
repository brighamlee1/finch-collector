from django.contrib import admin
from .models import Dog 
from .models import Puppy 
from .models import Litter 

admin.site.register(Dog)
admin.site.register(Puppy)
admin.site.register(Litter)
