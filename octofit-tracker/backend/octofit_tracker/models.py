from djongo import models


class User(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    profile = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)

    class Meta:
        db_table = 'teams'
        ordering = ['name']

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-date']

    def __str__(self):
        return f"{self.type} - {self.user_id}"


class Workout(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    exercises = models.JSONField(default=list)
    target_muscles = models.JSONField(default=list)
    equipment_needed = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'
        ordering = ['difficulty', 'name']

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.user_name} - Rank {self.rank}"
