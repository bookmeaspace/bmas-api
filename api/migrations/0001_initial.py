# Generated by Django 3.0.5 on 2020-07-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('numCourts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=100)),
                ('courtid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('members', models.ManyToManyField(to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
                ('time', models.IntegerField()),
                ('booker', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField()),
                ('courts', models.ManyToManyField(to='api.Court')),
            ],
        ),
    ]
