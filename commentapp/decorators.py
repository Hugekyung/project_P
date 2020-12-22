from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user: # 현재 유저가 리퀘스트를 요청한 유저와 동일한지 여부
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated