# Generated by Django 5.1.4 on 2024-12-19 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='awards/', verbose_name='Image')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('docs', models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Documents')),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('link', models.URLField(verbose_name='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partners/', verbose_name='Image')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biography')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='social_icons/', verbose_name='Icon')),
            ],
        ),
        migrations.CreateModel(
            name='AwardPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award_partners', to='api.award')),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award_partners', to='api.decision')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='award_partners', to='api.partner')),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='partners',
            field=models.ManyToManyField(related_name='awards', through='api.AwardPartner', to='api.partner', verbose_name='Partners'),
        ),
    ]
