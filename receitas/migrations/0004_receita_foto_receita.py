# Generated by Django 3.0.8 on 2020-08-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]