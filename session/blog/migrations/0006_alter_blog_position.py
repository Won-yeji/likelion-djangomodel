# Generated by Django 4.1.7 on 2023-03-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='position',
            field=models.CharField(choices=[('선택', 'None'), ('남자', '남자'), ('여자', '여자')], default='선택', max_length=10, verbose_name='성별'),
        ),
    ]
