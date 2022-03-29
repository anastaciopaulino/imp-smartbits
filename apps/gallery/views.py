from django.views import generic
from .models import Gallary

class GallaryListView(generic.ListView):
    context_object_name = 'photos'
    model = Gallary
    template_name = 'gallery/gallery.html'

    def  get_queryset(self):
        return self.model.objects.all()
