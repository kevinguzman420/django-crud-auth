from django.contrib import admin
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Tasks, TasksAdmin)  # to can see this model into the admin panel
