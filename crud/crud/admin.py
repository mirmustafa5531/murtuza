from django.contrib import admin
from .models import user 

@admin.register(user)

class UserAdmin(admin.ModelAdmin):
    list_disiplay = ('id','name','email','password')