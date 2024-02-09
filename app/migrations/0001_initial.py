# Generated by Django 4.2.7 on 2023-11-22 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=50)),
                ('skidka', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Korzina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('summa', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tovar')),
            ],
        ),
    ]
