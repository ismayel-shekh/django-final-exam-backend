# Generated by Django 4.2.4 on 2024-02-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participator', '0002_participator_complite_participator_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participator',
            old_name='complite',
            new_name='complete',
        ),
        migrations.AlterField(
            model_name='participator',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
