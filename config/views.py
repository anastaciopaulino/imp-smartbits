from django.views.generic import TemplateView
from apps.courses.models import Course
from apps.questions.models import Question
from apps.testimonials.models import Testimonial

class Home(TemplateView):
    template_name = 'config/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.all()
        context['questions'] = Question.objects.all()
        context['testimonials'] = Testimonial.objects.all()

        return context