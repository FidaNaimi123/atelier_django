from django.db import models
from categories.models import category
from django.core.validators import MaxValueValidator,FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Conference(models.Model):
     title=models.CharField(max_length=255)
     description=models.TextField()
     start_date=models.DateField(default=timezone.now().date())
     end_date=models.DateField(default=timezone.now().date())
     location=models.CharField(max_length=255)
     price=models.FloatField()
     capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=900,message='capacity must be under 900')])
     program = models.FileField(
        upload_to='files/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'], 
                message='Seuls les fichiers PDF, PNG, JPEG et JPG sont autorisés.'
            )
        ]
    )
     created_at=models.DateTimeField(auto_now_add=True)
     update_at=models.DateTimeField(auto_now=True)
     
     category=models.ForeignKey(category,on_delete=models.CASCADE,related_name="conferences")
     def clean(self):
          if self.end_date<=self.start_date :
               raise ValidationError('End date must be >star date ')
    
     class Meta:
           constraints = [
             models.CheckConstraint(
            check=models.Q(start_date__lte=models.F('end_date')),  
            name="start_date_before_end_date"
           )
           ]
   

     def __str__(self):
          return f"title conference {self.title} and location {self.location}"
     




     

