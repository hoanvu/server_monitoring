from django.contrib import admin
from .models import Server

class ServerAdmin(admin.ModelAdmin):
	list_display = ('servername', 'description')
	list_filter = ['servername']
	search_fields = ['servername']

# Register your models here.
admin.site.register(Server, ServerAdmin)