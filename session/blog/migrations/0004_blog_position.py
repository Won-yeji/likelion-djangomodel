# Generated by Django 4.1.7 on 2023-03-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='position',
            field=models.CharField(choices=[('선택', 'None'), ('남자', '남자'), ('여자', '여자')], default='선택', max_length=10),
        ),
    ]