# Generated by Django 3.2.1 on 2021-05-24 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0001_initial'),
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='leader',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ninjas.jouninninja'),
        ),
    ]