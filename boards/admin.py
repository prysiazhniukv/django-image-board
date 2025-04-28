from django.contrib import admin
from .models import Board, Thread


# Register your models her


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "updated_at", "slug")
    search_fields = ("title", "id")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "board", "created_at", "image")
    search_fields = ("title", "board__title")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
