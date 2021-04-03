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

    def __str__(self):
        return self.dog_name