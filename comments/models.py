from django.db import models
from accounts.models import User
from prototypes.models import Prototype

# Create your models here.
class Comment(models.Model):

  class Meta:
    db_table = 'comment'

  content = models.CharField(verbose_name='コメント', null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  prototype = models.ForeignKey(Prototype, on_delete=models.CASCADE)
