from django.views import generic
from .models import Event

class EventListView(generic.ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'events/events.html'

    def  get_queryset(self):
        return self.model.objects.all()
