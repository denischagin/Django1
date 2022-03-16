from django.contrib import admin

# Register your models here.
from .models import Firstapp, Comment

admin.site.register(Firstapp)
admin.site.register(Comment)