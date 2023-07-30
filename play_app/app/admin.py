from django.contrib import admin

from .models import FirstDatabase, SecondDatabase

# Register your models here.

admin.site.register(FirstDatabase)
admin.site.register(SecondDatabase)