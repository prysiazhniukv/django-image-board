from django.contrib import admin
from .models import boards


# Register your models her


@admin.register(boards)
class boardsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "updated_at")
    search_fields = ("title", "id")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
