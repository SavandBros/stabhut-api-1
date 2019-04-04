# Generated by Django 2.1.7 on 2019-03-22 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_type', models.PositiveIntegerField(choices=[(1, 'Card')], db_index=True)),
                ('for_object', models.TextField(db_index=True)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='label.Label')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]