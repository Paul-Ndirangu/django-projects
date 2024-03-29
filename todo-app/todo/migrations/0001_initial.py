# Generated by Django 5.0.1 on 2024-01-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('To Do', 'Todo'), ('Doing', 'Doing'), ('done', 'Done')], default='To Do', max_length=100)),
            ],
        ),
    ]
