# Generated by Django 3.0.2 on 2020-01-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200107_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='isbn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='type_publication',
            field=models.CharField(choices=[('B', 'Livre'), ('M', 'Musique'), ('F', 'Film'), ('_', 'Autre')], default='B', max_length=1),
        ),
    ]
