# Generated by Django 2.1.dev20180207233812 on 2018-02-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default='DEFAULT VALUE', null=True),
        ),
    ]
