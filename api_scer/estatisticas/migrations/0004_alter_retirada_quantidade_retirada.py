# Generated by Django 5.1.5 on 2025-01-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estatisticas', '0003_alter_produto_classificacao_alter_produto_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retirada',
            name='quantidade_retirada',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True),
        ),
    ]
