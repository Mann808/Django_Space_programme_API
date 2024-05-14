from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'interests', 'role']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

#-------------------------------------------------CRUD запросы-------------------------------------------------#

class SpaceMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceMission
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class SpacecraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spacecraft
        fields = '__all__'

class GalaxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galaxy
        fields = '__all__'

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

class AsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = '__all__'

class BlackHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackHole
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FavoriteSpaceObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSpaceObject
        fields = '__all__'

class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketDetail
        fields = '__all__'