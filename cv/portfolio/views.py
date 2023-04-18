from django.contrib import messages
from django.http import HttpRequest
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Education, WorkExperience, Contact


class ContextMixin:
    context = {
        'site_title': 'Portfolio',
        'full_name': 'Eugene Golnev',
        'job': 'Python Developer',
        'country': 'Poland',
        'tel': '+48 571 078 615',
        'email': 'eugenegolnev1993@gamil.com',
        'address': 'Poland, Wroclaw',
        'skills': {'Python': ['80', '1'], 'Django': ['65', '2'], 'FastAPI': ['60', '3'], 'SQL': ['60', '4'],
                   'Git': ['60', '5'], 'HTML5/CSS3': ['55', '6']},
    }


class MainTemplateView(ContextMixin, TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainTemplateView, self).get_context_data()
        context.update(self.context)
        context['Education'] = Education.objects.all().order_by('-id')
        context['WorkEx'] = WorkExperience.objects.all().order_by('-id')
        context['contact_form'] = ContactForm()
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for message!')
        else:
            messages.error(request, 'Something went wrong!')
        return self.get(request=request)
