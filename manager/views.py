from django.shortcuts import render, redirect
from django.apps import apps
Manager = apps.get_model('accounts', 'Manager')
Booking = apps.get_model('booking', 'Booking')
Rooms = apps.get_model('booking', 'Rooms')
import datetime
from django.contrib import messages
from datetime import date


def dashboard(request):
    if not request.session.get('username', None):
        return redirect('manager_login')
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')

    if request.session.get('username', None) and request.session.get('type', None) == 'manager':
        username = request.session['username']
        data = Manager.objects.get(username=username)
        room_data = data.rooms_set.all()
        booked = room_data.filter(is_available=False).count()

        context = {
           "room_data": room_data,
           "manager": data,
           "booked": booked
        }
        return render(request, "manager/index.html", context)

    else:
        return redirect("manager_login")


def add_room(request):
    if not request.session.get('username', None):
        return redirect('manager_login')
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    if request.method == "GET":
        return render(request, "manager/add-room.html", {})
    else:
        room_no = request.POST['room_no']
        room_type = request.POST['room_type']
        price = request.POST['price']
        image = request.FILES.get('image',None)
        no_of_days_advance = request.POST['no_of_days_advance']
        start_day = request.POST['start_day']
        error = []
        if(len(room_no)<1):
            messages.warning(request, "Room No Field must be atleast 3 digit like 100.")
        if(len(room_type)<5):
            error.append(1)
            messages.warning(request, "Select a valid Room Type.")
        if(len(price)<=2):
            error.append(1)
            messages.warning(request, "Please enter price")
        if(len(no_of_days_advance)<1):
            error.append(1)
            messages.warning(request, "Please add valid no of days a user can book room in advance.")
        if(len(start_day)<3):
            error.append(1)
            messages.warning(request, "Please add the starting day")
        if(not len(error)):
            manager = request.session['username']
            manager = Manager.objects.get(username=manager)
            room = Rooms(room_no=room_no, room_type=room_type, price=price, no_of_days_advance=no_of_days_advance,
                         start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),
                         image=image, manager=manager)
            room.save()
            messages.success(request, "Room Added Successfully")
            return redirect('manager_dashboard')
        else:
            return redirect('/manager/add/')


def update_room(request,room_no):
    if not request.session.get('username', None):
        return redirect('manager_login')
    if request.session.get('username', None) and request.session.get('type', None) == 'customer':
        return redirect('user_dashboard')
    room = Rooms.objects.get(room_no=room_no)
    if request.method == "GET":
        return render(request, "manager/edit-room.html", {"room": room})
    else:
        price = request.POST['price']
        no_of_days_advance = request.POST['no_of_days_advance']
        error = []
        if(len(price)<=2):
            error.append(1)
            messages.warning(request, "Please enter correct price")
        if(len(no_of_days_advance)<1):
            error.append(1)
            messages.warning(request, "Please add valid no of days a user can book room in advance.")
        if(not len(error)):
            manager = request.session['username']
            manager = Manager.objects.get(username=manager)
            room.price = price
            room.no_of_days_advance = no_of_days_advance
            room.save()
            messages.success(request, "Room Data Updated Successfully")
            return redirect('manager_dashboard')
        else:
            return redirect('/manager/add-room/update/' + room.room_no, {"room": room})

