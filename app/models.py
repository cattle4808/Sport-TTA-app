from django.db import models

class Status(models.TextChoices):
    admin = 'admin', 'Admin'
    user = 'user', 'User'

class UserModel(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.user)

    def __str__(self):
        return f'{self.telegram_id} - {self.username} - {self.status}'

class SportAreaModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SportAreaImagesModel(models.Model):
    sport_area = models.ForeignKey(SportAreaModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sport_area_images/')
    def __str__(self):
        return self.sport_area.name

class SessionAreaModel(models.Model):
    sport_area = models.ForeignKey(SportAreaModel, on_delete=models.CASCADE, related_name='session')
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} - {self.sport_area.name} - {self.day} - {self.start_time} - {self.end_time}'

class BookingModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    session_area = models.ForeignKey(SessionAreaModel, on_delete=models.CASCADE, related_name='session_area')
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.CharField(max_length=255, blank=True, null=True)
    students_count = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} - {self.user.telegram_id} - {self.session_area.sport_area.name} - {self.session_area.day} - {self.start_time} - {self.end_time}'


