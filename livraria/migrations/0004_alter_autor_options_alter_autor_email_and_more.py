# Generated by Django 5.0.6 on 2024-06-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_livro_autores'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
