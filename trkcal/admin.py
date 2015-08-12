from django.contrib import admin
from .models import Daily, Recurring, Due

admin.site.register(Daily)
admin.site.register(Due)
admin.site.register(Recurring)
