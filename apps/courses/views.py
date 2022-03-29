from email import message
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail

from .models import Course

from .forms import SubscriptionCreateForm

class CourseListView(generic.ListView):
    context_object_name = 'courses'
    model = Course
    template_name = 'courses/courses.html'

    def  get_queryset(self):
        return self.model.objects.all()

class SubscriptionCreateView(generic.CreateView):
    form_class = SubscriptionCreateForm
    success_url = reverse_lazy('courses:success')
    template_name = 'courses/subscription.html'

    def form_valid(self, form):
        self.object = form.save()

        message = f'O seu código de inscrição é: {self.object.code}'
        message_email = 'anastaciopaulino@gmail.com'

        print(message)
        # Send an email
        send_mail(
            "SmartBits Inscrição",
            message,
            message_email,
            ['euricopaulino87@gmail.com'],
        )

        return super().form_valid(form)

class Success(generic.TemplateView):
    template_name = 'courses/success.html'