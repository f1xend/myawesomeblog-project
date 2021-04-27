from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Schedule, Profile, ServiceBooking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import ProfileForm, BookingForm
from django.http import HttpResponseRedirect, request
from django.views.generic import UpdateView, View, CreateView, FormView
from django.urls import reverse
from django.urls import reverse_lazy
import services.views


# Create your views here.
def showservice(request):
    services = Service.objects
    return render(request, 'services/service.html', {'services': services})


def specific_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/specific_service.html', {'service': service})


def profile(UpdateView):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/service/profile/')
    else:
        form = ProfileForm()

    return render(request, 'services/profile.html', {'form': form})


# ээто отдельная вью
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'services/profile.html'
    # success_url = reverse('profile')
    success_url = reverse_lazy("profile_url")

    # def form_valid(self, form):
    # 	form.instance.user = self.request.user
    # 	return super(ProfileUpdate, self).form_valid(form)

    # get object
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class ServiceBookingAdd(LoginRequiredMixin, CreateView):
    # model = ServiceBooking
    # form_class = BookingForm
    # template_name = 'services/booking.html'
    login_url = reverse_lazy('account_login') # urls покажи где логинишься


    def get(self, request, *args, **kwargs):
        form = BookingForm()
        context = {
            'form': form,
        }
        return render(request, 'services/booking.html', context=context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            sb = form.save(commit=False)
            sb.user_id = request.user
            schedule = Schedule.objects.get(pk=sb.schedule_id.pk)
            schedule.schedule_waiting_status = False
            schedule.save()
            sb.save()
            return redirect('profile_url')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, 'services/booking.html', context=context)


        # def refirect(self):
        #     if Profile.phone_number = None
        #         return HttpResponseRedirect('/service/profile/')

    # fields = [
    #     'user_id',
    #     'service_id',
    #     'schedule_id',
    #     'booking_comment',
    # ]
    # def form_valid(self, request, form):
    #     print(form.user_id)
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #
    #     return super().form_valid(form)

    # def get_object(self):
    #     return get_object_or_404(ServiceBooking, user_id=self.request.user)
