# Generated by Django 3.1.2 on 2020-10-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20201014_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_From',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_Flags',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_Twitches',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Unique_Squirrel_ID',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
