from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input') # hello_world_input에 작성된 내용을 temp에 담는다

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save() # db에 저장한다

        return HttpResponseRedirect(reverse('accountapp:hello_world')) # accountapp안에 있는 hello_world의 url로 다시 돌아간다
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) # request를 받아서 내용을 base.html파일에서 가져온다.
        # return HttpResponse('안녕하세요') # 해당 모듈이 없을 때, alt+enter를 누르면 해당 모듈이 어떤 라이브러리에 있는지 자동으로 찾아준다.


class AccountCreateView(CreateView):
    model = User # 계정 만들기
    form_class = UserCreationForm # 계정 회원가입 폼
    success_url = reverse_lazy('accountapp:hello_world') # 성공 시 연결할 url
    # reverse를 클래스 내에서 그대로 사용할 수 없다(에러남)
    template_name = 'accountapp/create.html' # 어느 화면을 볼지