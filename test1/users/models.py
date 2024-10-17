from django.db import models
from django.contrib.auth.models import AbstractUser
from conferences.models import Conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.utils import timezone
def email_validator(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('Email invalid ,only @esprit.tn domaine')


class Participant(AbstractUser):
    cin_validator=RegexValidator(
        regex=r'^\d{8}$',message='this field must contain 8 dights'
    )
    cin = models.CharField(primary_key=True, max_length=8,validators=[cin_validator])
    email = models.EmailField(unique=True, max_length=255,validators=[email_validator])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    username = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'username'
    
    CHOICES = (
        ('etudiant', 'etudiant'),
        ('chercheur', 'chercheur'),
        ('docteur', 'docteur'),
        ('enseignant', 'enseignant'),
    )
    participant_category = models.CharField(max_length=255, choices=CHOICES)
    reservations=models.ManyToManyField(Conference,
                                    through='Reservation',
                                    related_name='Reservations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Reservation(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)  
    confirmed = models.BooleanField(default=False)
    reservation_date = models.DateTimeField(auto_now_add=True) 
    def clean(self):
        if self.conference.start_date<timezone.now().date():
            raise ValidationError('you can only reserve for upcoming')
        reservation_count=Reservation.objects.filter(
            participant=self.participant,

            reservation_date__date=timezone.now().date()
           
        )
        print("vide \n \n \n",len(reservation_count))
        if(len(reservation_count)+1>=3 ):
            raise ValidationError("you can only make up 3 reservations per day")

    class Meta:
        unique_together = (('conference', 'participant'),) 
    def __str__(self):
        return f"Reservation for {self.participant} at {self.conference} on {self.reservation_date}"

