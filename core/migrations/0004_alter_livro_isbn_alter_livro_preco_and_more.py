# Generated by Django 4.0.6 on 2022-07-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_autor_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
