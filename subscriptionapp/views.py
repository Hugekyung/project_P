from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscriptionapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # 존재하지 않는 projcet에 대해 구독을 하면 404에러페이지로 이동(예외처리)
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        if subscription.exists():
            subscription.delete() # 구독되어 있다면 구독 취소
        else:
            Subscription(user=user, project=project).save() # 없으면 구독하고 저장
        return super(SubscriptionView, self).get(request, *args, **kwargs)