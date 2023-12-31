# Generated by Django 4.2.3 on 2023-07-20 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('choosen_time', models.DateTimeField(auto_now_add=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bookings.department')),
            ],
        ),
    ]
