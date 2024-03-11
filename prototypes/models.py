from django.db import models
from accounts.models import User

# Create your models here.
class Prototype(models.Model):

  class Meta:
    db_table = 'prototype'

  title = models.CharField(verbose_name='タイトル', null=False)
  catch_copy = models.CharField(verbose_name='キャッチコピー', null=False)
  concept = models.CharField(verbose_name='コンセプト', null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images', verbose_name='画像', null=False)