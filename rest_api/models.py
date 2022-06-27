from django.db import models


class Directions(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    sort_number = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)
    description = models.TextField()
    date_of_birthday = models.DateField(max_length=10)
    work_experience = models.IntegerField()
    sort_number = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.direction} {self.slug}'
