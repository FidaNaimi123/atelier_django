from django.contrib import admin
from .models import Participant,Reservation
from conferences.models import Conference
from django.db.models import Count




class ReservationAdmin(admin.ModelAdmin):
    list_display=[ 'conference','participant_full_name','confirmed','reservation_date']
    
    def participant_full_name(self, obj):
        return f"{obj.participant.first_name} {obj.participant.last_name}"
    participant_full_name.short_description = 'Participant Full Name'
    @admin.action(description='Confirmer les réservations sélectionnées')
    def confirm_reservations(self, request, queryset):
        queryset.update(confirmed=True)
        self.message_user(request, f'{queryset.count()} réservations confirmées.')

    
    @admin.action(description='Non confirmer les réservations sélectionnées')
    def unconfirm_reservations(self, request, queryset):
        queryset.update(confirmed=False)
        self.message_user(request, f'{queryset.count()} réservations non confirmées.')
    actions = [confirm_reservations, unconfirm_reservations]


class ReservationFilter(admin.SimpleListFilter):
    title = 'Reservation_number'
    parameter_name = 'Reservation'

    def lookups(self, request, model_admin):
        return (
            ('0', 'no_Reservation'),
            ('more', 'more than one Reservation'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.annotate(reservation_count=Count('reservation')).filter(reservation_count=0)

        if self.value() == 'more':
            return queryset.annotate(reservation_count=Count('reservation')).filter(reservation_count__gt=0)

class ParticipantAdmin(admin.ModelAdmin):
    def reservation_count(self, obj):
        
        return obj.reservations.count()
    list_display=[ 'first_name','last_name','email','participant_category','reservation_count']


    list_filter = ['first_name',ReservationFilter]
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page = 10
    fieldsets = (
    ('Personal Information', {
        'fields': ('first_name', 'last_name', 'cin', 'email', 'username')
    }),
    ('Category and Participation', {
        'fields': ('participant_category',)
    }),
   
)

   
    
    



        



admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Reservation,ReservationAdmin)




