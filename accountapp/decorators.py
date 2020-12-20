from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user: # 현재 유저가 리퀘스트를 요청한 유저와 동일한지 여부
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated