from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from config import settings
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token = default_token_generator.make_token(user)
        activation_url = reverse_lazy(
            'users:email_verified', kwargs={'token': user.token}
        )
        send_mail(
            subject="Подтверждение почты",
            message=f"Ссылка: http://localhost:8000/{activation_url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.save()
        return redirect('users:email_conf_sent')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/email_conf_sent.html'


class UserConfirmEmailView(View):
    def get(self, request, token):
        user = User.objects.get(token=token)

        user.is_active = True
        user.token = None
        user.save()
        return redirect('users:login')


class EmailConfirmView(TemplateView):
    template_name = 'users/email_verified.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        return context


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

