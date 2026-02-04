from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Workout, Leaderboard
from datetime import datetime


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            _id='test_user_1',
            name='Test User',
            email='test@example.com',
            password='hashed_password',
            team_id='test_team_1',
            profile={'age': 25, 'fitness_level': 'Beginner'}
        )

    def test_get_users_list(self):
        """Test retrieving list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        """Test retrieving a specific user"""
        url = reverse('user-detail', args=[self.user._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test User')

    def test_create_user(self):
        """Test creating a new user"""
        url = reverse('user-list')
        data = {
            '_id': 'test_user_2',
            'name': 'New User',
            'email': 'new@example.com',
            'password': 'hashed_password',
            'team_id': 'test_team_1',
            'profile': {'age': 30}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            _id='test_team_1',
            name='Test Team',
            description='A test team',
            members=['test_user_1', 'test_user_2']
        )

    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_team_detail(self):
        """Test retrieving a specific team"""
        url = reverse('team-detail', args=[self.team._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Team')


class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(
            _id='test_activity_1',
            user_id='test_user_1',
            type='Running',
            duration_minutes=30,
            calories_burned=250,
            distance_km=5.0,
            date=datetime.now(),
            notes='Test run'
        )

    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_activity_detail(self):
        """Test retrieving a specific activity"""
        url = reverse('activity-detail', args=[self.activity._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Running')

    def test_filter_activities_by_user(self):
        """Test filtering activities by user_id"""
        url = reverse('activity-by-user')
        response = self.client.get(url, {'user_id': 'test_user_1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            _id='test_workout_1',
            name='Test Workout',
            description='A test workout',
            difficulty='Beginner',
            duration_minutes=30,
            exercises=[{'name': 'Push-ups', 'sets': 3, 'reps': 10}],
            target_muscles=['Chest', 'Arms'],
            equipment_needed=['None']
        )

    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_workout_detail(self):
        """Test retrieving a specific workout"""
        url = reverse('workout-detail', args=[self.workout._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Workout')

    def test_filter_workouts_by_difficulty(self):
        """Test filtering workouts by difficulty"""
        url = reverse('workout-by-difficulty')
        response = self.client.get(url, {'difficulty': 'Beginner'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.leaderboard_entry = Leaderboard.objects.create(
            _id='test_leaderboard_1',
            user_id='test_user_1',
            user_name='Test User',
            team_id='test_team_1',
            total_activities=10,
            total_calories=2000,
            total_duration_minutes=300,
            rank=1
        )

    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_leaderboard_detail(self):
        """Test retrieving a specific leaderboard entry"""
        url = reverse('leaderboard-detail', args=[self.leaderboard_entry._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_name'], 'Test User')

    def test_get_top_leaderboard(self):
        """Test retrieving top N leaderboard entries"""
        url = reverse('leaderboard-top')
        response = self.client.get(url, {'limit': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) <= 5)


class APIRootTestCase(APITestCase):
    def test_api_root(self):
        """Test API root endpoint"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)
