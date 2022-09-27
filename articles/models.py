from django.db import models

# Create your models here.
class Article(models.Model): #상속
    #id는 자동 생성됨. 아래 세 가지가 가장 많이 쓰이는 모델필드이다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
