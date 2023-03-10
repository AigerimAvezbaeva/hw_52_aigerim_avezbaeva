# Generated by Django 4.1.6 on 2023-02-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0003_alter_todoparagraph_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoparagraph',
            name='completion_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='todoparagraph',
            name='title',
            field=models.CharField(max_length=400, verbose_name='Задача'),
        ),
    ]
