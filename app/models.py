from django.db import models

class Status(models.TextChoices):
    admin = 'admin', 'Admin'
    user = 'user', 'User'

class UserModel(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.user)

    def __str__(self):
        return self.username

class SportAreaModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SessionAreaModel(models.Model):
    sport_area = models.ForeignKey(SportAreaModel, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.sport_area} - {self.start_time} - {self.end_time}"

class BookingModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    session_area = models.ForeignKey(SessionAreaModel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user} - {self.session_area} - {self.start_time} - {self.end_time}"