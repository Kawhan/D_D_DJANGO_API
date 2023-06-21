from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=250)
    race = models.CharField(max_length=70)
    strength = models.FloatField()
    dexterity = models.FloatField()
    construction = models.FloatField()
    intelligence = models.FloatField()
    wisdom = models.FloatField()
    armor_class = models.FloatField()
    initiative = models.FloatField()
    displacement = models.FloatField()
    max_life_point = models.FloatField()
    current_life_points = models.FloatField()
    points_life_temp = models.FloatField()
    equipment = models.TextField()
    traits_personality = models.TextField()
    ideals = models.TextField()
    links = models.TextField()
    weaknesses = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.race
