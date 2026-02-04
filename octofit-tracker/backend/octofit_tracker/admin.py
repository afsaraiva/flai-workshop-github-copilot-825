from django.contrib import admin
from .models import User, Team, Activity, Workout, Leaderboard


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'email', 'team_id', 'created_at']
    list_filter = ['team_id', 'created_at']
    search_fields = ['name', 'email', '_id']
    readonly_fields = ['created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'description', 'created_at']
    search_fields = ['name', '_id']
    readonly_fields = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user_id', 'type', 'duration_minutes', 'calories_burned', 'date']
    list_filter = ['type', 'date']
    search_fields = ['user_id', 'type', '_id']
    date_hierarchy = 'date'


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'difficulty', 'duration_minutes', 'created_at']
    list_filter = ['difficulty', 'created_at']
    search_fields = ['name', '_id']
    readonly_fields = ['created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user_name', 'team_id', 'rank', 'total_calories', 'total_activities', 'updated_at']
    list_filter = ['team_id', 'updated_at']
    search_fields = ['user_name', 'user_id', '_id']
    readonly_fields = ['updated_at']
    ordering = ['rank']
