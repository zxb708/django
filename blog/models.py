from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
    ## 作者 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ## 标题
    title = models.CharField(max_length=200)
    ## 文本
    text = models.TextField()
    ## 创建时间
    created_data = models.DateTimeField(default=timezone.now)
    ## 发布时间
    published_data = models.DateTimeField(blank=True, null=True)


    ## 定义方法,published_data 赋值
    def publish(self):
        self.published_data = timezone.now()
        self.save()

    ##
    def __str__(self):
        return self.title
