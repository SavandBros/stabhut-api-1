# Generated by Django 3.0.1 on 2020-03-26 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20191223_1832'),
        ('milestone', '0002_auto_20200326_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilestoneCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Card')),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone.Milestone')),
            ],
        ),
    ]
