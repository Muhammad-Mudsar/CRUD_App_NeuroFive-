from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import EventsForm, registerForm, EventEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Events
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# from django.http import HttpResponse


# Create your views here.

""""
#My Events CRUD App Home Page
"""


def index(request):

    return render(request, "esapp/index.html")
    # dict key:value  ,above key=>'title'


def ex(request):

    return render(request, "esapp/ex.html")
    # dict key:value  ,above key=>'title'


def events(request):
    if request.user.is_authenticated:
        events = Events.objects.all().order_by("-date").filter(user=request.user)
        # (new 1st user specific Events)

        return render(request, "esapp/events.html", {"events": events})

    else:
        events = Events.objects.all().order_by("-date")  # (descending - new 1st)
    return render(request, "esapp/events.html", {"events": events})


class EventDetailView(View):
    def get(self, request, pk):
        eventD = Events.objects.get(pk=pk)

        return render(
            request,
            "esapp/eventdetail.html",
            {
                "event": eventD,
            },
        )


@method_decorator(login_required, name="dispatch")
class create(View):
    def get(self, request):
        form = EventsForm()
        return render(
            request,
            "esapp/create-event.html",
            {"form": form},
        )

    def post(self, request):
        form = EventsForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, "New Event Scheduled Successfully!")
        else:
            return render(request, "esapp/create-event.html", {"form": form})

        return render(request, "esapp/create-event.html", {"form": form})
        # pass blank form


# views.py - Simple2v
# from django.contrib.auth.views import LoginView
# from django.urls import reverse
# class CustomLoginView(LoginView):
#     def get_success_url(self):
#         user = self.request.user
#         # Check for staff or manager role
#         if (
#             user.is_staff
#             or user.is_superuser
#             or user.groups.filter(name="Managers").exists()
#         ):
#             return reverse("dashboard")
#         return reverse("index")

############### test stack

# class CustomLoginView(LoginView):
#     def get_success_url(self):
#         user = self.request.user

#         # Check for staff or manager role
#         if (
#             user.is_staff
#             or user.is_superuser
#             or user.groups.filter(name="Managers").exists()
#         ):
#             return reverse("dashboard")  # Redirect to dashboard
#         return reverse("home")  # Redirect to home page


# user  login
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return render(request, "esapp/login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if (
                user.is_staff
                or user.is_superuser
                or user.groups.filter(name="Managers").exists()
            ):
                messages.success(request, "You have been logged in successfully.")
                return redirect("dashboard")
            else:
                messages.success(request, "You have been logged in successfully.")
            return redirect("index")

        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "esapp/login.html")
    else:
        return render(request, "esapp/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You Are Now LogedOut")
    return redirect("index")


def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            messages.success(request, "You Are Now Registered")
            login(request, user)
        # redirect('login')
    else:
        form = registerForm()
    return render(request, "esapp/register.html", {"form": form})


# Admin staff / Organizers


@login_required
def dashboard(request):
    events = Events.objects.all()
    return render(request, "esapp/dashboard.html", {"events": events})


@login_required
def manage_events(request):

    search_term = request.GET.get("search","").strip()
    #status = request.GET.get("statusFilter")
    cat = request.GET.get("statusFilter", "").strip()
    
    if search_term:
       # events = Events.objects.filter ( Q (title__icontains=search_term) | Q(category__icontains=cat))
        events = Events.objects.filter( Q(title__icontains=search_term) | Q(description__icontains=search_term)
            | Q(category__icontains=cat)
        )
    elif cat:
        events = Events.objects.filter( Q(title__icontains=search_term) & Q(category__icontains=cat))

    else:    
        
        # fetch events data
        events = Events.objects.all().order_by("-date")
    return render(
        request, "esapp/manage-events.html", {"user": request.user, "events": events}
    )


def event_edit(request, id):
    event = get_object_or_404(Events, id=id)

    if request.method == "POST":
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated Successfully")
            return redirect("manageE")
    else:
        form = EventEditForm(instance=event)

    return render(request, "esapp/event_edit.html", {"form": form})


def event_delete(request, id):
    event = get_object_or_404(Events, id=id)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect("dashboard")

    return render(request, "esapp/event_confirm_delete.html", {"event": event})


# regs
@login_required
def my_registrations(request):
    events = request.user.registered_events.all()
    return render(request, "esapp/my_registrations.html", {"events": events})


@login_required
def cancel_registration(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.user not in event.registered_users.all():
        messages.error(request, "You are not registered for this event.")
        return redirect("my_registrations")

    if request.method == "POST":
        event.registered_users.remove(request.user)
        messages.success(request, "Registration cancelled successfully.")

    return redirect("my_registrations")
