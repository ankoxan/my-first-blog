from django.db import models
from django.utils import timezone


class Postan(models.Model):
    QQQ = models.ForeignKey('auth.User')
    WWWW = models.CharField(max_length=200)
    EEE = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title