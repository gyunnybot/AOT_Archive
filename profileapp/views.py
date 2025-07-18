from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls.base import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

@method_decorator(login_required, 'dispatch')
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    # 클라이언트 본인의 프로필만 생성할 수 있도록 서버에서 관리
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(login_required, 'dispatch')
@method_decorator(profile_ownership_required, 'dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})