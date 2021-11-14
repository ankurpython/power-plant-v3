from django.db import models

# Create your models here.


class PowerGenerator(models.Model):
    data_year = models.IntegerField(null=True)
    plant_state = models.CharField(max_length=100, null=True)
    plant_name = models.CharField(max_length=250, null=True)
    plant_code = models.IntegerField(null=True)
    gen_id = models.CharField(max_length=100, null=True)
    num_boilers = models.PositiveBigIntegerField(null=True)
    gen_status = models.CharField(max_length=10, null=True)
    gen_type = models.CharField(max_length=10, null=True)
    gen_fuel = models.CharField(max_length=50, null=True)
    gen_capacity = models.FloatField(null=True)
    gen_capacity_factor = models.FloatField(null=True)
    annual_net_gen = models.FloatField(null=True)
    ozone_season_ng = models.FloatField(null=True)
    data_source = models.CharField(max_length=250, null=True)
    year_on_line = models.IntegerField(null=True)
    retirement_year = models.IntegerField(null=True)