from django.db import models
from malmesbury_tandoori.custom_fields import CurrencyField
from taggit.managers import TaggableManager


SPICE_CHOICES = (
            ('mild','Mild'),
            ('medium','Medium'),
            ('hot','Hot'),
            ('very_hot','Fairly Hot'),
            ('none',None)
        )
CATEGORY_TYPE_CHOICES = (
            ('starter','Starters'),
            ('special','Specials'),
            ('main','Mains'),
            ('sides','Sides and Extras')
        )
# Create your models here.
class FoodItem(models.Model):
    class Meta:
        verbose_name = "FoodItem"
        verbose_name_plural = "FoodItems"

    name = models.CharField(max_length=128)
    price = CurrencyField(max_digits=4,decimal_places=2,currency_symbol='£')
    description = models.TextField(blank=True)
    FoodCategory = models.ForeignKey('FoodCategory', related_name='items')
    tags = TaggableManager()
    spice_rating = models.IntegerField()

    def __str__(self):
        return self.name

class FoodCategory(models.Model):

    class Meta:
        verbose_name = "FoodCategory"
        verbose_name_plural = "FoodCategories"

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,default=None,null=True)
    spice_description = models.CharField(max_length=64,choices=SPICE_CHOICES, default='none',null=True)
    categoryType =  models.CharField(max_length=128, choices=CATEGORY_TYPE_CHOICES)
    def get_spice_description(self):
        if not self.get_spice_description_display():
            return ""
        return "("+self.get_spice_description_display()+")"
    def __str__(self):
        return self.name
   
