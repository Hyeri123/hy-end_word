# Generated by Django 5.1.3 on 2024-12-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_word_user_alter_word_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='user',
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]