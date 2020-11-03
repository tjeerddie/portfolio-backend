# Generated by Django 3.1.2 on 2020-10-28 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=120)),
                ('summary', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('source', models.URLField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('private', models.BooleanField(default=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_admin.portfolio')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
