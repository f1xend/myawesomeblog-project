from django import forms
from .models import Profile, ServiceBooking, Schedule


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'phone_number', 'first_name', 'last_name']
        fields_required = ['phone_number', 'first_name']


# class BookingForm(forms.ModelForm):
# 	class Meta:
# 		model = ServiceBooking
# 		fields = ['__all__']
# 		# exclude = ['user_id']

class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schedule_id'].queryset = Schedule.objects.filter(schedule_waiting_status=True)

    class Meta:
        model = ServiceBooking
        fields = ['service_id', 'schedule_id', 'booking_comment']
        exclude = ['user_id']
