# Generated by Django 3.1.2 on 2020-11-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_admin', '0003_auto_20201103_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('network', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('url', models.URLField(blank=True)),
                ('private', models.BooleanField(default=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_admin.portfolio')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
