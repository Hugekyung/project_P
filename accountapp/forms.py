from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 함수 초기화
        
        self.fields['username'].disabled = True # 유저아이디 수정 불가 옵션 true 설정