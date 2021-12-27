from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import datetime
from .models import Contact, Rooms, Booking, News
from django.views.generic import DeleteView
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.apps import apps
User = apps.get_model('accounts', 'Customer')


def home(request):
    if request.method == "POST":
        message = "i want to subscribe to your newsletter alerts"
        name = request.POST['name']
        email = request.POST['email']
        news = News(name=name, email=email)
        news.save()
        send_mail(
            'Newsletter Subscription',
            message,
            email,
            ['chuksmbanasoj@gmail.com'],
            fail_silently=True
        )
        messages.success(request, f"Thanks for subscribing to our newsletter!! {name}")
        return redirect("home")
    return render(request, "booking/home.html", {})


def contact_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST.get('phone_no', False)
        message = request.POST['message']
        contact = Contact(name=username, email=email, message=message, phone_no=phone_no)
        contact.save()
        send_mail(
            'Contact Inquiry',
            message,
            email,
            ['chuksmbanasoj@gmail.com'],
            fail_silently=True
        )
        messages.success(request, 'Thank you for contacting us, the manager will get back to you soon')
        return redirect('/contact/')
    return render(request, "booking/contact.html", {})


def book_view(request):
    if request.method == "POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        request.session['start_date'] = start_date
        request.session['end_date'] = end_date
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        no_of_days = (end_date-start_date).days
        date = Rooms.objects.filter(
            is_available=True,
            no_of_days_advance__gte=no_of_days,
            start_date__lte=start_date
        ).order_by('room_no')
        request.session['no_of_days'] = no_of_days

        paginator = Paginator(date, 6)
        page = request.GET.get('page')
        date_page = paginator.get_page(page)

        context = {
           'data': date_page,
        }
        return render(request, 'booking/book.html', context)
    else:
        return redirect('home')


def book_now(request, id):
    if request.session.get("username", None) and request.session.get("type", None) == 'customer':
        if request.session.get("no_of_days", 1):
            no_of_days = request.session['no_of_days']
            start_date = request.session['start_date']
            end_date = request.session['end_date']
            request.session['room_no'] = id
            data = Rooms.objects.get(room_no=id)
            bill = data.price*int(no_of_days)
            request.session['bill'] = bill
            room_manager = data.manager.username

            context = {
               "no_of_days": no_of_days,
               "room_no": id,
               "data": data,
               "bill": bill,
               "room_manager": room_manager,
               "start": start_date,
               "end": end_date,
            }
            return render(request, "booking/book-now.html", context)
        else:
            return redirect("home")
    else:
        return redirect('user_login')


def book_confirm(request):
    room_no = request.session['room_no']
    start_date = request.session['start_date']
    end_date = request.session['end_date']
    username = request.session['username']
    user_id = User.objects.get(username=username)
    room = Rooms.objects.get(room_no=room_no)
    amount = request.session['bill']
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    data = Booking(room_no=room, start_day=start_date, end_day=end_date, amount=amount, user_id=user_id)
    data.save()
    room.is_available = False
    room.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['room_no']
    messages.info(request, "Room has been successfully booked")
    return redirect('user_dashboard')


class CancelRoom(DeleteView):
    model = Booking
    template_name = "booking/cancel-room.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Booking, id=id)

    def get_success_url(self):
        messages.add_message(self.request, messages.WARNING, f"Room has been cancelled")
        return "/customers/home/"


class DeleteRoom(DeleteView):
    model = Rooms
    template_name = "booking/delete-room.html"

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Rooms, id=id)

    def get_success_url(self):
        messages.add_message(self.request, messages.WARNING, f"Room has been deleted")
        return "/manager/dashboard/"


