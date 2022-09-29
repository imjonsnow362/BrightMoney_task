# Generated by Django 3.0.7 on 2020-07-18 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0007_budgetcategoryamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetcategoryamount',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myfinance.Category', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
