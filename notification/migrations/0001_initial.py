# Generated by Django 3.1.7 on 2021-03-05 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tweet', '0002_auto_20210301_2116'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_tweet', to='tweet.tweet')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
