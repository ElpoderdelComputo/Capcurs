# Generated by Django 4.1.7 on 2023-03-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capcursapp', '0004_alter_capcurs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='coordinaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_campus', models.CharField(max_length=3)),
                ('cve_posgrad', models.CharField(max_length=6)),
                ('nom_posgra', models.CharField(max_length=60)),
                ('cve_program', models.CharField(max_length=3)),
                ('nom_program', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
