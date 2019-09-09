from django.contrib import admin
from .models import Breif, Client, Plan, PlanOverView

# Register your models here
admin.site.register(Breif)
admin.site.register(Client)
admin.site.register(Plan)
admin.site.register(PlanOverView)
