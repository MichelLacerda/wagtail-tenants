# Generated by Django 3.2.18 on 2023-09-20 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20230920_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tenants', to='customers.clientfeaturegroup'),
        ),
    ]