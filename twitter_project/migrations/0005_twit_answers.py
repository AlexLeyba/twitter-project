# Generated by Django 2.0.7 on 2018-07-13 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_project', '0004_auto_20180712_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='answers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter_project.Twit', verbose_name='Ответы'),
        ),
    ]
