from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        self.stdout.write(self.style.SUCCESS('Connected to MongoDB'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field for users collection
        db.users.create_index([("email", 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Insert Teams
        self.stdout.write('Inserting teams...')
        teams = [
            {
                "_id": "team_marvel",
                "name": "Team Marvel",
                "description": "Defenders of the Earth",
                "created_at": datetime.now(),
                "members": []
            },
            {
                "_id": "team_dc",
                "name": "Team DC",
                "description": "Justice League United",
                "created_at": datetime.now(),
                "members": []
            }
        ]
        db.teams.insert_many(teams)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(teams)} teams'))

        # Insert Users
        self.stdout.write('Inserting users...')
        users = [
            # Marvel Team
            {
                "_id": "user_ironman",
                "name": "Tony Stark",
                "email": "tony@avengers.com",
                "password": "hashed_password_123",
                "team_id": "team_marvel",
                "profile": {
                    "age": 48,
                    "height": 185,
                    "weight": 85,
                    "fitness_level": "Advanced"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_spiderman",
                "name": "Peter Parker",
                "email": "peter@avengers.com",
                "password": "hashed_password_123",
                "team_id": "team_marvel",
                "profile": {
                    "age": 23,
                    "height": 178,
                    "weight": 76,
                    "fitness_level": "Advanced"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_blackwidow",
                "name": "Natasha Romanoff",
                "email": "natasha@avengers.com",
                "password": "hashed_password_123",
                "team_id": "team_marvel",
                "profile": {
                    "age": 35,
                    "height": 170,
                    "weight": 61,
                    "fitness_level": "Expert"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_hulk",
                "name": "Bruce Banner",
                "email": "bruce@avengers.com",
                "password": "hashed_password_123",
                "team_id": "team_marvel",
                "profile": {
                    "age": 45,
                    "height": 175,
                    "weight": 128,
                    "fitness_level": "Advanced"
                },
                "created_at": datetime.now()
            },
            # DC Team
            {
                "_id": "user_batman",
                "name": "Bruce Wayne",
                "email": "bruce@justiceleague.com",
                "password": "hashed_password_123",
                "team_id": "team_dc",
                "profile": {
                    "age": 42,
                    "height": 188,
                    "weight": 95,
                    "fitness_level": "Expert"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_superman",
                "name": "Clark Kent",
                "email": "clark@justiceleague.com",
                "password": "hashed_password_123",
                "team_id": "team_dc",
                "profile": {
                    "age": 35,
                    "height": 191,
                    "weight": 107,
                    "fitness_level": "Expert"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_wonderwoman",
                "name": "Diana Prince",
                "email": "diana@justiceleague.com",
                "password": "hashed_password_123",
                "team_id": "team_dc",
                "profile": {
                    "age": 5000,
                    "height": 183,
                    "weight": 75,
                    "fitness_level": "Godlike"
                },
                "created_at": datetime.now()
            },
            {
                "_id": "user_flash",
                "name": "Barry Allen",
                "email": "barry@justiceleague.com",
                "password": "hashed_password_123",
                "team_id": "team_dc",
                "profile": {
                    "age": 28,
                    "height": 183,
                    "weight": 81,
                    "fitness_level": "Advanced"
                },
                "created_at": datetime.now()
            }
        ]
        db.users.insert_many(users)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(users)} users'))

        # Update teams with member references
        db.teams.update_one(
            {"_id": "team_marvel"},
            {"$set": {"members": ["user_ironman", "user_spiderman", "user_blackwidow", "user_hulk"]}}
        )
        db.teams.update_one(
            {"_id": "team_dc"},
            {"$set": {"members": ["user_batman", "user_superman", "user_wonderwoman", "user_flash"]}}
        )

        # Insert Activities
        self.stdout.write('Inserting activities...')
        activities = []
        activity_types = ["Running", "Cycling", "Swimming", "Weight Training", "Yoga", "Boxing"]
        
        for i, user_id in enumerate(["user_ironman", "user_spiderman", "user_blackwidow", "user_hulk", 
                                      "user_batman", "user_superman", "user_wonderwoman", "user_flash"]):
            for j in range(5):
                activities.append({
                    "_id": f"activity_{user_id}_{j}",
                    "user_id": user_id,
                    "type": activity_types[j % len(activity_types)],
                    "duration_minutes": 30 + (j * 10),
                    "calories_burned": 200 + (j * 50),
                    "distance_km": 5 + (j * 2) if j % 2 == 0 else None,
                    "date": datetime.now() - timedelta(days=j),
                    "notes": f"Great {activity_types[j % len(activity_types)].lower()} session!"
                })
        
        db.activities.insert_many(activities)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(activities)} activities'))

        # Insert Workouts
        self.stdout.write('Inserting workouts...')
        workouts = [
            {
                "_id": "workout_beginner_cardio",
                "name": "Beginner Cardio Blast",
                "description": "Perfect for getting started with cardio fitness",
                "difficulty": "Beginner",
                "duration_minutes": 30,
                "exercises": [
                    {"name": "Jumping Jacks", "sets": 3, "reps": 20},
                    {"name": "High Knees", "sets": 3, "duration_seconds": 30},
                    {"name": "Burpees", "sets": 3, "reps": 10}
                ],
                "target_muscles": ["Legs", "Core", "Cardio"],
                "equipment_needed": ["None"],
                "created_at": datetime.now()
            },
            {
                "_id": "workout_strength_upper",
                "name": "Upper Body Strength",
                "description": "Build strength in your upper body",
                "difficulty": "Intermediate",
                "duration_minutes": 45,
                "exercises": [
                    {"name": "Push-ups", "sets": 4, "reps": 15},
                    {"name": "Pull-ups", "sets": 4, "reps": 8},
                    {"name": "Dumbbell Press", "sets": 4, "reps": 12}
                ],
                "target_muscles": ["Chest", "Back", "Arms", "Shoulders"],
                "equipment_needed": ["Pull-up bar", "Dumbbells"],
                "created_at": datetime.now()
            },
            {
                "_id": "workout_hero_training",
                "name": "Superhero Training",
                "description": "Train like a superhero with this intense workout",
                "difficulty": "Advanced",
                "duration_minutes": 60,
                "exercises": [
                    {"name": "Box Jumps", "sets": 5, "reps": 15},
                    {"name": "Deadlifts", "sets": 5, "reps": 10},
                    {"name": "Battle Ropes", "sets": 5, "duration_seconds": 45},
                    {"name": "Plank", "sets": 5, "duration_seconds": 60}
                ],
                "target_muscles": ["Full Body"],
                "equipment_needed": ["Box", "Barbell", "Battle Ropes"],
                "created_at": datetime.now()
            },
            {
                "_id": "workout_flexibility",
                "name": "Flexibility and Mobility",
                "description": "Improve your range of motion and flexibility",
                "difficulty": "Beginner",
                "duration_minutes": 30,
                "exercises": [
                    {"name": "Cat-Cow Stretch", "sets": 3, "reps": 10},
                    {"name": "Downward Dog", "sets": 3, "duration_seconds": 30},
                    {"name": "Hip Flexor Stretch", "sets": 3, "duration_seconds": 45}
                ],
                "target_muscles": ["Back", "Hips", "Legs"],
                "equipment_needed": ["Yoga mat"],
                "created_at": datetime.now()
            },
            {
                "_id": "workout_speed_agility",
                "name": "Speed and Agility Training",
                "description": "Perfect for athletes looking to improve speed",
                "difficulty": "Advanced",
                "duration_minutes": 40,
                "exercises": [
                    {"name": "Sprint Intervals", "sets": 8, "duration_seconds": 30},
                    {"name": "Ladder Drills", "sets": 5, "reps": 10},
                    {"name": "Cone Drills", "sets": 5, "reps": 10}
                ],
                "target_muscles": ["Legs", "Core", "Cardio"],
                "equipment_needed": ["Agility ladder", "Cones"],
                "created_at": datetime.now()
            }
        ]
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(workouts)} workouts'))

        # Calculate and insert Leaderboard entries
        self.stdout.write('Calculating leaderboard...')
        leaderboard_entries = []
        
        for user in users:
            user_activities = [a for a in activities if a['user_id'] == user['_id']]
            total_calories = sum(a['calories_burned'] for a in user_activities)
            total_duration = sum(a['duration_minutes'] for a in user_activities)
            total_activities = len(user_activities)
            
            leaderboard_entries.append({
                "_id": f"leaderboard_{user['_id']}",
                "user_id": user['_id'],
                "user_name": user['name'],
                "team_id": user['team_id'],
                "total_activities": total_activities,
                "total_calories": total_calories,
                "total_duration_minutes": total_duration,
                "rank": 0,  # Will be updated after sorting
                "updated_at": datetime.now()
            })
        
        # Sort by total calories and assign ranks
        leaderboard_entries.sort(key=lambda x: x['total_calories'], reverse=True)
        for i, entry in enumerate(leaderboard_entries):
            entry['rank'] = i + 1
        
        db.leaderboard.insert_many(leaderboard_entries)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(leaderboard_entries)} leaderboard entries'))

        # Close connection
        client.close()

        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams: {len(teams)}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {len(users)}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {len(activities)}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {len(workouts)}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {len(leaderboard_entries)}'))
