from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): # 모델폼을 상속받아서 간단하게 폼을 만들 수 있다.
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']