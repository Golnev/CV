# Generated by Django 4.1.6 on 2023-02-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='number',
            field=models.TextField(default=1, verbose_name='String number of education'),
            preserve_default=False,
        ),
    ]
