from django.contrib import admin
from . import models

#관리자 페이지에서 만든 모델을 보려면 admin.site.register(Post)로 모델을 등록해야 해요.
admin.site.register(models.Post)
admin.site.register(models.GuestBook)
admin.site.register(models.Reply)