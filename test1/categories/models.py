from django.db import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError

# Create your models here.
# Create your models here
def lettre_only(value):
    if not re.match(r'^[A-Za-z\s]+$',value):
        raise ValidationError('only letters are allowed')

class category(models.Model):


    title=models.CharField(unique=True,max_length=255,validators=[lettre_only])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('title',)
        verbose_name = "Publication"
        verbose_name_plural = "Publications"  
    

    