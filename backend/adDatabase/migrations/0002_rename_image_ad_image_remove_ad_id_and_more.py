# Generated by Django 4.0.4 on 2022-04-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adDatabase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='Image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='id',
        ),
        migrations.AddField(
            model_name='ad',
            name='auto_increment_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
