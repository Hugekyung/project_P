from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # OneToOneField: user와 1:1로 정보 매칭, on_delete=models.CASCADE 해당 User가 삭제될 때 매칭된 정보도 함께 삭제하는 옵션.
    
    image = models.ImageField(upload_to='profile/', null=True) # 프로필 이미지가 저장되는 경로
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
