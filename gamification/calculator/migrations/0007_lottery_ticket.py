# Generated by Django 3.2.8 on 2021-11-02 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_auto_20211030_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('write_off', models.DecimalField(decimal_places=2, max_digits=7)),
                ('referral_coeff', models.PositiveIntegerField(blank=True, null=True)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('min_profit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('min_rentability', models.DecimalField(decimal_places=2, max_digits=3)),
                ('max_rentability', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('lottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lottery_items', to='calculator.lottery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lottery_items', to='calculator.product')),
            ],
        ),
    ]