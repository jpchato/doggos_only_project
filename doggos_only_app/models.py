from django.db import models

# Create your models here.
SIZE = (
    ('tiny', 'tiny'),
    ('small', 'small'),
    ('medium', 'medium'),
    ('large', 'large'),
    ('hecca big boi', 'hecca big boi')
)
class Dog(models.Model):
    dog_picture = models.ImageField(upload_to = 'images/', default = None)
    dog_name = models.CharField(max_length = 40)
    class Size(models.TextChoices):
        SMALL = 'Small',
        MEDIUM = 'Medium',
        LARGE = 'Large'
    dog_size = models.CharField(
        choices = Size.choices,
        blank = True,
        null = True,
        max_length = 255
    )
    class Demeanor(models.TextChoices):
        PLAYFUL = 'Playful',
        NERVOUS = 'Nervous',
        ANXIOUS = 'Anxious',
        EXCITABLE = 'Excitable',
        PATIENT = 'Patient',
        AGGRESSIVE = 'Aggressive',
    demeanor = models.CharField(
        choices = Demeanor.choices,
        blank = True,
        null = True,
        max_length = 255
    )
    city = models.CharField(max_length = 100, default = None)
    state = models.CharField(max_length = 100, default = None)


    def __str__(self):
        return self.dog_name