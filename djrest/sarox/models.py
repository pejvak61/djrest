from django.db import models

# Create your models here.
class SaroxUsers(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    salt = models.CharField(db_column='Salt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sarox_users'