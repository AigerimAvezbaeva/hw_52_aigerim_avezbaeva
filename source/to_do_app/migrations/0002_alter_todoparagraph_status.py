# Generated by Django 4.1.6 on 2023-02-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoparagraph',
            name='status',
            field=models.CharField(choices=[('in_process', 'В процессе'), ('new', 'Новая'), ('complete', 'Завершена')], default='new', max_length=50, verbose_name='Статус задачи'),
        ),
    ]