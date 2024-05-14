from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = 'Roles'

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    interests = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.username
    
class SpaceMission(models.Model):
    name = models.CharField(max_length=255)
    launch_date = models.DateField()
    objective = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    participating_countries = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Space_Missions'

    def __str__(self):
        return self.name

class Photo(models.Model):
    mission = models.ForeignKey(SpaceMission, on_delete=models.CASCADE)
    object_type = models.CharField(max_length=50)
    capture_date = models.DateField()
    photo_link = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Photos'

    def __str__(self):
        return self.object_type

class Spacecraft(models.Model):
    name = models.CharField(max_length=255)
    launch_date = models.DateField()
    type = models.CharField(max_length=50)
    mission = models.ForeignKey(SpaceMission, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Spacecrafts'

    def __str__(self):
        return self.name

class Galaxy(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, blank=True, null=True)
    size = models.FloatField()
    distance_from_earth = models.FloatField()
    number_of_stars = models.BigIntegerField()
    has_black_hole = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Galaxies'

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=255)
    diameter = models.FloatField()
    mass = models.FloatField()
    average_distance_from_sun = models.FloatField()
    orbital_period = models.FloatField()
    number_of_moons = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Planets'

    def __str__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(max_length=255)
    spectral_class = models.CharField(max_length=50, blank=True, null=True)
    surface_temperature = models.FloatField()
    luminosity = models.FloatField()
    distance_from_earth = models.FloatField(blank=True, null=True)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Stars'

    def __str__(self):
        return self.name

class Asteroid(models.Model):
    name = models.CharField(max_length=255)
    diameter = models.FloatField()
    mass = models.FloatField()
    orbit = models.CharField(max_length=255)
    discovery_date = models.DateField()
    potential_hazard = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Asteroids'

    def __str__(self):
        return self.name

class BlackHole(models.Model):
    name = models.CharField(max_length=255)
    mass = models.FloatField()
    distance_from_earth = models.FloatField()
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Black_Holes'

    def __str__(self):
        return self.name

class FavoriteSpaceObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space_object_id = models.IntegerField()
    object_type = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Favorite_Space_Objects'

class TicketStatus(models.Model):
    name = models.CharField(max_length=255, unique=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Ticket_Status'

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateField()
    number_of_tickets = models.IntegerField()
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Tickets'

class TicketDetail(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=255)
    price = models.FloatField()
    departure_planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='departure_planet')
    destination_planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='destination_planet')
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'Ticket_Details'
