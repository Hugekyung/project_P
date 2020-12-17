from django.db import models

# Create your models here.
# 데이터를 관리하는 모델(db와 연결)

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)