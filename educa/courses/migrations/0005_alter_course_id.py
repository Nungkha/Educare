# Generated by Django 4.1 on 2023-08-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
