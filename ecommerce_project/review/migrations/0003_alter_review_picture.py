# Generated by Django 5.1.3 on 2024-11-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='review/'),
        ),
    ]
