from django.db import models

class UserInput(models.Model):
    def __str__(self):
        return self.name

    IMAGE_TYPES = (
        ('spiral', 'Spiral'),
        ('wave', 'Wave'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    image_type = models.CharField(max_length=100, choices=IMAGE_TYPES, default='Spiral')
    image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=10, blank=True, null=True)
