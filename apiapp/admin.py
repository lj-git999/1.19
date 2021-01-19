from django.contrib import admin

# Register your models here.
from apiapp import models

admin.site.register(models.User)