from rest_framework import generics, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=serializer.validated_data['username'])
        salt = make_password(None)
        password = make_password(serializer.validated_data['password'], salt=salt)
        user.password = password
        user.salt = salt
        user.save()
        refresh = RefreshToken.for_user(user)
        headers = self.get_success_headers(serializer.data)
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response.data.update({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        return response

class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if user and check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#-------------------------------------------------CRUD запросы-------------------------------------------------#

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class LogicalDeleteViewMixin:
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

class LogicalRestoreViewMixin:
    def perform_update(self, serializer):
        serializer.save(deleted=False)

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.filter(deleted=False)
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'name']
    ordering_fields = ['username', 'name']
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpaceMissionListCreate(generics.ListCreateAPIView):
    queryset = SpaceMission.objects.filter(deleted=False)
    serializer_class = SpaceMissionSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'participating_countries']
    ordering_fields = ['name', 'launch_date']

class SpaceMissionRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SpaceMission.objects.all()
    serializer_class = SpaceMissionSerializer

class PhotoListCreate(generics.ListCreateAPIView):
    queryset = Photo.objects.filter(deleted=False)
    serializer_class = PhotoSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['object_type', 'photo_link']
    ordering_fields = ['capture_date']

class PhotoRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class SpacecraftListCreate(generics.ListCreateAPIView):
    queryset = Spacecraft.objects.filter(deleted=False)
    serializer_class = SpacecraftSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type']
    ordering_fields = ['name', 'launch_date']

class SpacecraftRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializer

class GalaxyListCreate(generics.ListCreateAPIView):
    queryset = Galaxy.objects.filter(deleted=False)
    serializer_class = GalaxySerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type']
    ordering_fields = ['name', 'distance_from_earth']

class GalaxyRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer

class PlanetListCreate(generics.ListCreateAPIView):
    queryset = Planet.objects.filter(deleted=False)
    serializer_class = PlanetSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'diameter']

class PlanetRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class StarListCreate(generics.ListCreateAPIView):
    queryset = Star.objects.filter(deleted=False)
    serializer_class = StarSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'spectral_class']
    ordering_fields = ['name', 'luminosity']

class StarRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer

class AsteroidListCreate(generics.ListCreateAPIView):
    queryset = Asteroid.objects.filter(deleted=False)
    serializer_class = AsteroidSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'orbit']
    ordering_fields = ['name']

class AsteroidRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Asteroid.objects.all()
    serializer_class = AsteroidSerializer

class BlackHoleListCreate(generics.ListCreateAPIView):
    queryset = BlackHole.objects.filter(deleted=False)
    serializer_class = BlackHoleSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'mass']

class BlackHoleRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = BlackHole.objects.all()
    serializer_class = BlackHoleSerializer

class RoleListCreate(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class RoleRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class FavoriteSpaceObjectListCreate(generics.ListCreateAPIView):
    queryset = FavoriteSpaceObject.objects.filter(deleted=False)
    serializer_class = FavoriteSpaceObjectSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['object_type']
    ordering_fields = ['user', 'object_type']

class FavoriteSpaceObjectRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteSpaceObject.objects.all()
    serializer_class = FavoriteSpaceObjectSerializer

class TicketStatusListCreate(generics.ListCreateAPIView):
    queryset = TicketStatus.objects.filter(deleted=False)
    serializer_class = TicketStatusSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class TicketStatusRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer

class TicketListCreate(generics.ListCreateAPIView):
    queryset = Ticket.objects.filter(deleted=False)
    serializer_class = TicketSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['number_of_tickets', 'sale_date']

class TicketRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailListCreate(generics.ListCreateAPIView):
    queryset = TicketDetail.objects.filter(deleted=False)
    serializer_class = TicketDetailSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['passenger_name']
    ordering_fields = ['passenger_name', 'price']

class TicketDetailRetrieveUpdateDestroy(LogicalDeleteViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketDetail.objects.all()
    serializer_class = TicketDetailSerializer