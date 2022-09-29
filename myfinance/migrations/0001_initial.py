# Generated by Django 3.0.7 on 2020-06-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_desc', models.CharField(max_length=200)),
                ('updated_desc', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('category', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
