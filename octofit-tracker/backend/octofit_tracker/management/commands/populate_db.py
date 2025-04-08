from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data safely
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Populate users
        for user_data in test_users:
            User.objects.get_or_create(**user_data)

        # Populate teams
        for team_data in test_teams:
            Team.objects.get_or_create(**team_data)

        # Ensure user is saved before creating activities
        for activity_data in test_activities:
            user_email = activity_data.pop("user")
            user, _ = User.objects.get_or_create(email=user_email)
            user.save()  # Ensure the user is saved
            Activity.objects.get_or_create(user=user, **activity_data)

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.get_or_create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.get_or_create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database successfully populated with test data.'))