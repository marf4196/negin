from django.contrib import admin
from .models import Posts

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug','description', 'created_time', 'updated_time']
    search_fields = ['title', 'slug', 'description']
    date_hierarchy = 'created_time'
    ordering = ['-created_time']
admin.site.register(Posts, postAdmin)