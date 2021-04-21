from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def booking_seat_new(request):
    form = PostForm()
    return render(request, 'booking/booking_seat_edit.html', {'form': form})