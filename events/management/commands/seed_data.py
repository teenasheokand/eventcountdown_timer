from django.core.management.base import BaseCommand
from events.models import Event
from datetime import date, time

class Command(BaseCommand):
    help = "Add sample events"

    def handle(self, *args, **kwargs):
        if Event.objects.exists():
            self.stdout.write(self.style.WARNING("Sample data already exists."))
            return

        Event.objects.create(
            title="College Tech Fest",
            date=date(2026, 10, 15),
            time=time(10, 0),
            location="College Auditorium",
            description="A fun technology event with projects and presentations."
        )
        Event.objects.create(
            title="Birthday Party",
            date=date(2026, 10, 20),
            time=time(18, 30),
            location="Community Hall",
            description="Birthday celebration with friends and family."
        )
        Event.objects.create(
            title="Project Presentation",
            date=date(2026, 10, 25),
            time=time(11, 0),
            location="Computer Lab",
            description="Django project demonstration and viva."
        )

        self.stdout.write(self.style.SUCCESS("3 sample events added successfully."))
