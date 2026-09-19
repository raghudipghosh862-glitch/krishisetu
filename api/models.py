from django.db import models

class GroupLeader(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.district}"

class Farmer(models.Model):
    # Matches the 'Onboard Farmer' modal from profile.html
    krishi_id = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    primary_crop = models.CharField(max_length=50)
    
    # GPS Coordinates for OR-Tools Routing & Leaflet Maps
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.krishi_id})"


class HarvestLog(models.Model):
    # Matches the 'Log Harvest' form
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="harvests")
    crop_type = models.CharField(max_length=50)
    quality_grade = models.CharField(max_length=20)
    weight_kg = models.FloatField()
    expected_price_per_kg = models.FloatField(null=True, blank=True)
    
    # Status tracking for the Escrow system
    status = models.CharField(max_length=30, default="Pending Pooling")
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.weight_kg}kg of {self.crop_type} - {self.farmer.krishi_id}"
    
class TransportCompany(models.Model):
    company_name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=100) # Base city/district
    fleet_size = models.IntegerField(default=1)
    rate_per_km = models.DecimalField(max_digits=6, decimal_places=2) # e.g., 40.50 Rs/km
    trust_rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)

class Driver(models.Model):
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    # If null, they are an independent local driver hired off-platform
    transport_company = models.ForeignKey(TransportCompany, on_delete=models.SET_NULL, null=True, blank=True)
    current_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class Trip(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Company Approval'),
        ('ACCEPTED', 'Accepted - Awaiting Advance'),
        ('ADVANCE_PAID', 'Advance Paid - Truck Released'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered - Awaiting Verification'),
        ('COMPLETED', 'Completed & Final Payment Escrow Released')
    ]
    
    group_leader = models.ForeignKey(GroupLeader, on_delete=models.CASCADE)
    transport_company = models.ForeignKey(TransportCompany, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    cargo_weight_kg = models.IntegerField()
    
    estimated_distance_km = models.DecimalField(max_digits=6, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    is_off_platform_booking = models.BooleanField(default=False)
class MarketPost(models.Model):
    POST_TYPES = [
        ('SELL', 'Group Leader Selling'),
        ('BUY', 'Buyer Looking for Crops')
    ]
    
    post_type = models.CharField(max_length=4, choices=POST_TYPES)
    poster_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    
    # Comma-separated list of crops (e.g., "Onion, Potato")
    crop_names = models.CharField(max_length=255) 
    quantity_kg = models.IntegerField(help_text="Expected quantity in KG")
    
    # SELLER FIELDS
    ai_suggested_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    available_from = models.DateField(null=True, blank=True)
    expires_on = models.DateField(null=True, blank=True) # Spoiling date
    
    # BUYER FIELDS
    delivery_location = models.CharField(max_length=200, null=True, blank=True)
    needed_by_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Shows newest posts first, like LinkedIn