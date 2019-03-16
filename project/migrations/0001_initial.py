# Generated by Django 2.1.7 on 2019-03-16 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
            ],
        ),
    ]
