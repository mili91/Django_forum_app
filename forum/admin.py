from django.contrib import admin
from .models import Thread, Reply


admin.site.register(Thread)
admin.site.register(Reply)