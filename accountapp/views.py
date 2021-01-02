from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

# @login_required 비login 상태일 때 hello_world 페이지에 접속하면 login.html로 이동하게 하는 Decorator

class AccountCreateView(CreateView):
    model = User # 계정 만들기
    form_class = UserCreationForm # 계정 회원가입 폼
    success_url = reverse_lazy('home') # 성공 시 연결할 url
    # reverse를 클래스 내에서 그대로 사용할 수 없다(에러남)
    template_name = 'accountapp/create.html' # 어느 화면을 볼지

# login과 logout은 따로 클래스 지정 없이 바로 urls.py에서 import해주면 된다.

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # 다른 유저가 내 페이지에 왔을 때, target_user인 나의 정보를 보여주도록
    template_name = 'accountapp/detail.html'
    
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home') # 성공 시 연결할 url
    # reverse를 클래스 내에서 그대로 사용할 수 없다(에러남)
    template_name = 'accountapp/update.html' # 어느 화면을 볼지


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login') # 성공 시 연결할 url
    # reverse를 클래스 내에서 그대로 사용할 수 없다(에러남)
    template_name = 'accountapp/delete.html' # 어느 화면을 볼지

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()