# Generated by Django 5.0.6 on 2024-09-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-date']},
        ),
    ]
