from django import forms
from .models import Seat as SeatModel , Booking as BookingModel, BookingSeat as BookingSeatModel

class SeatForm(forms.ModelForm):
    class Meta:
        model = SeatModel
        fields = ('seat_type',)

class SelectedSeatForm(forms.Form):
    selected_seat = forms.CharField(required=True,max_length=10,help_text='Seat No seperated by ,')

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ('payment_type',)
