# Generated by Django 4.1.1 on 2022-11-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_App_2', '0002_alter_autos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='foto',
            field=models.ImageField(upload_to='media/foto'),
        ),
    ]
