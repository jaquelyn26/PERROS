# Generated by Django 2.0.6 on 2021-09-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webperros', '0006_auto_20210904_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='img',
            field=models.URLField(default='https://i.postimg.cc/xjH36Tw2/2222222222.jpg', max_length=8000),
        ),
    ]