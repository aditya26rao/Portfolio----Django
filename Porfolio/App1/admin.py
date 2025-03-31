from django.contrib import admin
from App1.models import Portfolio
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display=['name','email','comments']
admin.site.register(Portfolio,PortfolioAdmin)