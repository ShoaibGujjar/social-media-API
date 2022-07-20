from django.contrib import admin
from .models import CustomUser,UserImage

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserImage)