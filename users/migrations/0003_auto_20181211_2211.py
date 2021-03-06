# Generated by Django 2.1.2 on 2018-12-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fluent_languages',
            field=models.ManyToManyField(related_name='fluent_users', to='users.Language'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='learning_languages',
            field=models.ManyToManyField(related_name='learning_users', to='users.Language'),
        ),
    ]
