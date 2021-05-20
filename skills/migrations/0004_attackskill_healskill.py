# Generated by Django 3.1.5 on 2021-05-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_parchment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttackSkill',
            fields=[
                ('skill_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skills.skill')),
                ('range', models.IntegerField()),
            ],
            bases=('skills.skill',),
        ),
        migrations.CreateModel(
            name='HealSkill',
            fields=[
                ('skill_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skills.skill')),
                ('speed', models.IntegerField()),
            ],
            bases=('skills.skill',),
        ),
    ]