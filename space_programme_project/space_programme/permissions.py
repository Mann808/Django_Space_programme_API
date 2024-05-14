from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *

class IsGuestUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            token = request.auth.split()[1]
            payload = RefreshToken(token).payload
            user_roles = User.objects.get(id=payload['user_id']).role.name
            return user_roles == 'Guest'
        except:
            return False

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            token = request.auth.split()[1]
            payload = RefreshToken(token).payload
            user_roles = User.objects.get(id=payload['user_id']).role.name
            return user_roles == 'User'
        except:
            return False

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            token = request.auth.split()[1]
            payload = RefreshToken(token).payload
            user_roles = User.objects.get(id=payload['user_id']).role.name
            return user_roles == 'Administrator'
        except:
            return False