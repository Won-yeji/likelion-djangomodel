from django.db import models

class Blog(models.Model):
  title = models.CharField('제목', max_length=100)
  position_choices = [
    ('선택', 'None'), ('남자', '남자'), ('여자', '여자')
  ]
  position = models.CharField('성별', max_length=10, choices = position_choices, default='선택')
  introduce = models.TextField('내용')
  birthdate = models.DateField('생일', null=True)

  def __str__(self):
    return self.title