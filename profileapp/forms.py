from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): # 모델폼을 상속받아서 간단하게 폼을 만들 수 있다.
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message'] # user정보까지 넘겨주면, 타인의 정보를 수정할 우려가 있기 때문에 user정보는 따로 처리