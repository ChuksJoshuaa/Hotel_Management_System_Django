import datetime
from django.shortcuts import render, redirect
from django.apps import apps
User = apps.get_model('accounts', 'Customer')
Booking = apps.get_model('booking', 'Booking')


def user_dashboard(request):
   if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        return redirect('manager_dashboard')
   if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        username = request.session['username']
        data = User.objects.get(username=username)
        booking_data = Booking.objects.filter(user_id=data).order_by('-id')
        counts = booking_data.filter(end_day__lt=datetime.datetime.now()).count()
        available = len(booking_data)-counts

        context = {
           "data": booking_data,
           "count": counts,
           "available": available,
        }
        return render(request, "customer/index.html", context)

   else:
      return redirect("user_login")


def user_detail(request, id, booking_id):
    if not request.session.get('username',None):
        return redirect('manager_login')
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    try:
        booking_data = Booking.objects.get(id=booking_id)
        user = User.objects.get(id=id)
        context = {
           "user": user,
           "booking_data": booking_data,
        }
        return render(request, "customer/detail.html", context)

    except:
        return redirect("/manager/dashboard/")


