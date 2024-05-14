from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('space_missions/', views.SpaceMissionListCreate.as_view(), name='space_mission-list-create'),
    path('space_missions/<int:pk>/', views.SpaceMissionRetrieveUpdateDestroy.as_view(), name='space_mission-retrieve-update-destroy'),
    path('photos/', views.PhotoListCreate.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', views.PhotoRetrieveUpdateDestroy.as_view(), name='photo-retrieve-update-destroy'),
    path('spacecrafts/', views.SpacecraftListCreate.as_view(), name='spacecraft-list-create'),
    path('spacecrafts/<int:pk>/', views.SpacecraftRetrieveUpdateDestroy.as_view(), name='spacecraft-retrieve-update-destroy'),
    path('galaxies/', views.GalaxyListCreate.as_view(), name='galaxy-list-create'),
    path('galaxies/<int:pk>/', views.GalaxyRetrieveUpdateDestroy.as_view(), name='galaxy-retrieve-update-destroy'),
    path('planets/', views.PlanetListCreate.as_view(), name='planet-list-create'),
    path('planets/<int:pk>/', views.PlanetRetrieveUpdateDestroy.as_view(), name='planet-retrieve-update-destroy'),
    path('stars/', views.StarListCreate.as_view(), name='star-list-create'),
    path('stars/<int:pk>/', views.StarRetrieveUpdateDestroy.as_view(), name='star-retrieve-update-destroy'),
    path('asteroids/', views.AsteroidListCreate.as_view(), name='asteroid-list-create'),
    path('asteroids/<int:pk>/', views.AsteroidRetrieveUpdateDestroy.as_view(), name='asteroid-retrieve-update-destroy'),
    path('black_holes/', views.BlackHoleListCreate.as_view(), name='black_hole-list-create'),
    path('black_holes/<int:pk>/', views.BlackHoleRetrieveUpdateDestroy.as_view(), name='black_hole-retrieve-update-destroy'),
    path('roles/', views.RoleListCreate.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleRetrieveUpdateDestroy.as_view(), name='role-retrieve-update-destroy'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('favorite_space_objects/', views.FavoriteSpaceObjectListCreate.as_view(), name='favorite_space_object-list-create'),
    path('favorite_space_objects/<int:pk>/', views.FavoriteSpaceObjectRetrieveUpdateDestroy.as_view(), name='favorite_space_object-retrieve-update-destroy'),
    path('ticket_statuses/', views.TicketStatusListCreate.as_view(), name='ticket_status-list-create'),
    path('ticket_statuses/<int:pk>/', views.TicketStatusRetrieveUpdateDestroy.as_view(), name='ticket_status-retrieve-update-destroy'),
    path('tickets/', views.TicketListCreate.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', views.TicketRetrieveUpdateDestroy.as_view(), name='ticket-retrieve-update-destroy'),
    path('ticket_details/', views.TicketDetailListCreate.as_view(), name='ticket_detail-list-create'),
    path('ticket_details/<int:pk>/', views.TicketDetailRetrieveUpdateDestroy.as_view(), name='ticket_detail-retrieve-update-destroy'),
]