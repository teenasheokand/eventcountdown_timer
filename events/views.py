from django.shortcuts import get_object_or_404, redirect, render
from .models import Event

def event_list(request):
    events = Event.objects.order_by("date", "time")
    return render(request, "events/event_list.html", {"events": events})

def add_event(request):
    if request.method == "POST":
        Event.objects.create(
            title=request.POST["title"],
            date=request.POST["date"],
            time=request.POST["time"],
            location=request.POST["location"],
            description=request.POST.get("description", ""),
        )
        return redirect("event_list")
    return render(request, "events/event_form.html", {"page_title": "Add Event"})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.title = request.POST["title"]
        event.date = request.POST["date"]
        event.time = request.POST["time"]
        event.location = request.POST["location"]
        event.description = request.POST.get("description", "")
        event.save()
        return redirect("event_list")

    return render(
        request,
        "events/event_form.html",
        {"page_title": "Edit Event", "event": event},
    )

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.delete()
        return redirect("event_list")

    return render(request, "events/event_list.html", {
        "events": Event.objects.order_by("date", "time"),
        "delete_event": event,
    })
