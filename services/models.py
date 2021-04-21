from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Service(models.Model):
	service_title = models.CharField(max_length=300)
	service_time = models.TimeField()
	service_text = models.TextField()
	service_image = models.ImageField(upload_to='service_images/')
	# service_number = models.SlugField(primary_key=True)

	def get_summary(self):
		return self.service_text[:70]


	def __str__(self):
		return self.service_title

class Schedule(models.Model):
	# service = models.ForeignKey(Service, on_delete=models.CASCADE)
	schedule_date = models.DateField(u'Day of the event', help_text=u'Day of the event')
	schedule_timefrom = models.TimeField(u'Starting time', help_text=u'Starting time')
	schedule_timeto = models.TimeField(u'Final time', help_text=u'Final time')
	schedule_waiting_status = models.BooleanField(default=True)
	schedule_notes = models.CharField (max_length=300, help_text=u'Textual Notes', blank=True, default='free')

	def __str__(self):
		return f'{self.schedule_timefrom}:{self.schedule_timeto}'

	class Meta:
		verbose_name = u'Scheduling'
		verbose_name_plural = u'Scheduling'

	def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
		overlap = False
		if new_start == fixed_end or new_end == fixed_start:  #edge case
			overlap = False
		elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
			overlap = True
		elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
			overlap = True
		return overlap

	def get_absolute_url(self):
		url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
		return u'<a href="%s">%s</a>' % (url, str(self.schedule_timefrom))

	def clean(self):
		if self.schedule_timeto <= self.schedule_timefrom:
			raise ValidationError("Ending times must after starting times")

		# events = Schedule.objects.filter(schedule_date=self.schedule_date)
		# if events.exists():
		# 	for event in events:
		# 		if self.check_overlap(event.schedule_timefrom, event.schedule_timeto, self.schedule_timefrom, self.schedule_timeto):
		# 			raise ValidationError(
  #       				'There is an overlap with another event: ' + str(event.schedule_date) + ', ' + str(
  #       					event.schedule_timefrom) + '-' + str(event.schedule_timeto))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    birth_date = models.DateField(null=True, blank=True, help_text='DD.MM.YYYY')
    phone_number = PhoneNumberField(blank=True, null=True, help_text='+79998887766')
    first_name = models.CharField(max_length=300, null=True, help_text='Иван')
    last_name = models.CharField(max_length=300, null=True, help_text='Иванов')

    # class Meta:
    # 	def __str__(self):
    # 		return: self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class ServiceBooking(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
	schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
	booking_comment = models.CharField (max_length=300, help_text=u'Textual Notes', blank=True, default=u'Свободно')
	booking_date = models.DateTimeField(auto_now_add=True)



# @receiver(post_save, sender=Schedule)
# def set_schedule_waiting_status(sender, instance, **kwargs):
#     instance.profile.save()