# Generated by Django 3.2.1 on 2021-05-21 00:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invocations', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('clan', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField(verbose_name='birth')),
                ('gender', models.CharField(max_length=10)),
                ('invocations', models.ManyToManyField(blank=True, to='invocations.Invocation')),
                ('skills', models.ManyToManyField(blank=True, to='skills.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('in_mission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChuninNinja',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ninjas.ninja')),
                ('exam_date', models.DateField()),
                ('classification', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            bases=('ninjas.ninja',),
        ),
        migrations.CreateModel(
            name='GeninNinja',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ninjas.ninja')),
                ('graduation_date', models.DateField()),
                ('assessment', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            bases=('ninjas.ninja',),
        ),
        migrations.CreateModel(
            name='HokageNinja',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ninjas.ninja')),
                ('hokage_number', models.IntegerField()),
            ],
            bases=('ninjas.ninja',),
        ),
        migrations.CreateModel(
            name='JouninNinja',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ninjas.ninja')),
                ('exam_date', models.DateField()),
                ('classification', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            bases=('ninjas.ninja',),
        ),
        migrations.AddField(
            model_name='ninja',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ninjas.team'),
        ),
        migrations.AddField(
            model_name='ninja',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
