# Generated by Django 4.2.4 on 2024-02-25 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_question_choice_question_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.AddField(
            model_name='review',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer_Name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
