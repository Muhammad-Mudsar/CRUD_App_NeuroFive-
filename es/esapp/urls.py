from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ex", views.ex, name="ex"),
    path("events", views.events, name="events"),
    path(
        "event-detail/<int:pk>",
        views.EventDetailView.as_view(),
        name="event-detail",
    ),
    path("create", views.create.as_view(), name="create"),
    # simple version of Auth
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("manage", views.manage_events, name="manageE"),
    path("events/edit/<int:id>/", views.event_edit, name="event_edit"),
    path("events/delete/<int:id>/", views.event_delete, name="event_delete"),
    path("my-registrations/", views.my_registrations, name="my_registrations"),
    path(
        "cancel-registration/<int:event_id>/",
        views.cancel_registration,
        name="cancel_registration",
    ),
]
