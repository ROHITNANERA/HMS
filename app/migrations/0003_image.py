# Generated by Django 4.0.2 on 2022-04-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_room_capacity_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=200)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hostel')),
            ],
        ),
    ]
