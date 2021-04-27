import datetime

from django import forms
from .models import Profile, ServiceBooking, Schedule
from phonenumber_field.formfields import PhoneNumberField
from django.utils import timezone
import phonenumbers


class ProfileForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        phone_number = self.cleaned_data.get("phone_number")
        num = '+7'
        if num in phone_number and len(phone_number) == 12 and phone_number[1:12].isdigit():
            return cleaned_data
        else:
            raise forms.ValidationError("Введите корректный номер телефона!")

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
        # q1 = Schedule.objects.filter(self.fields.schedule_date>=datetime.date.today())
        self.fields['schedule_id'].queryset = Schedule.objects.filter(schedule_waiting_status=True).filter(
            schedule_date__gt=datetime.datetime.now())
        # self.fields['schedule_id'].queryset = Schedule.objects.filter(schedule_waiting_status=True)

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        booking_phone = self.cleaned_data.get("booking_phone")
        num = '+7'
        if num in booking_phone and len(booking_phone) == 12 and booking_phone[1:12].isdigit():
            return cleaned_data
        else:
            raise forms.ValidationError("Введите корректный номер телефона!")

    class Meta:
        model = ServiceBooking
        fields = ['service_id', 'schedule_id', 'booking_comment', 'booking_phone']
        exclude = ['user_id']

    # def clean_phone(self):
    #     booking_phone = self.cleaned_data.get("booking_phone")
    #     z = phonenumbers.parse(booking_phone, "RU")
    #     if not phonenumbers.is_valid_number(z):
    #         self.add_error("network", "Number not in RU format")
    #         # raise forms.ValidationError("Number not in RU format")
    #     return booking_phone
    #

    # def form_valid(self, form):
    #     print('метод вызвался')
    #     form_valid = super().form_valid(form)
    #     phone_num = form.cleaned_data['booking_phone']
    #     print(phone_num)
    #     num = '+7'
    #     if phone_num is not num and len(phone_num) != 12:
    #         print('не валидна')
    #         pass
    #         # self.form_invalid(self)
    #     else:
    #         print('валидна')
    #         # return form_valid
    #         pass
