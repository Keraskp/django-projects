from django.db import models

# Create your models here.
class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(default=0)
    item_description = models.TextField(default='')

    def __str__(self) -> str:
        return self.item_id