# Generated by Django 4.0 on 2024-04-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_remove_candidateapplications_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectcandidatejob',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('selected', 'selected')], default='pending', max_length=20),
        ),
    ]