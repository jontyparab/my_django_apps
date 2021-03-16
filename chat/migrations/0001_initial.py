# Generated by Django 3.1.7 on 2021-03-16 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statususerone', models.BooleanField(default=False)),
                ('statususertwo', models.BooleanField(default=False)),
                ('userone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_requester', to=settings.AUTH_USER_MODEL)),
                ('usertwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_requestee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='friend',
            constraint=models.UniqueConstraint(fields=('userone', 'usertwo'), name='unique_record'),
        ),
    ]