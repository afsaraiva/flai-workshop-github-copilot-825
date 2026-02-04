from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    WorkoutSerializer, LeaderboardSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific user"""
        user = self.get_object()
        activities = Activity.objects.filter(user_id=user._id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        """Get statistics for a specific user"""
        user = self.get_object()
        leaderboard_entry = Leaderboard.objects.filter(user_id=user._id).first()
        if leaderboard_entry:
            serializer = LeaderboardSerializer(leaderboard_entry)
            return Response(serializer.data)
        return Response({'message': 'No stats available'}, status=status.HTTP_404_NOT_FOUND)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get all members of a team"""
        team = self.get_object()
        users = User.objects.filter(team_id=team._id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def leaderboard(self, request, pk=None):
        """Get leaderboard for a specific team"""
        team = self.get_object()
        leaderboard = Leaderboard.objects.filter(team_id=team._id)
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities filtered by user_id query parameter"""
        user_id = request.query_params.get('user_id', None)
        if user_id:
            activities = Activity.objects.filter(user_id=user_id)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'user_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get activities filtered by type query parameter"""
        activity_type = request.query_params.get('type', None)
        if activity_type:
            activities = Activity.objects.filter(type=activity_type)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'type parameter required'}, status=status.HTTP_400_BAD_REQUEST)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts filtered by difficulty query parameter"""
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            workouts = Workout.objects.filter(difficulty=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'difficulty parameter required'}, status=status.HTTP_400_BAD_REQUEST)


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top N entries from leaderboard"""
        limit = int(request.query_params.get('limit', 10))
        leaderboard = Leaderboard.objects.all()[:limit]
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard filtered by team_id query parameter"""
        team_id = request.query_params.get('team_id', None)
        if team_id:
            leaderboard = Leaderboard.objects.filter(team_id=team_id)
            serializer = self.get_serializer(leaderboard, many=True)
            return Response(serializer.data)
        return Response({'error': 'team_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)
