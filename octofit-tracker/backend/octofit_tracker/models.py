from djongo import models
from djongo.models import ObjectIdField

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    team = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)  # Use ObjectId for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.user.name}: {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name