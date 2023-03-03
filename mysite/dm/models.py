from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'USERS'

    name = models.CharField(max_length=30)
