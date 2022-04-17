# Generated by Django 4.0.3 on 2022-04-16 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_grade_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='comment',
            field=models.TextField(),
        ),
    ]