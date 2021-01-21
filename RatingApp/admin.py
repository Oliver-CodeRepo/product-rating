from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user_email','rate','review','product','user','date_created')
    list_display = ['product','user','review','rate','date_created']
    list_filter = []

admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)
