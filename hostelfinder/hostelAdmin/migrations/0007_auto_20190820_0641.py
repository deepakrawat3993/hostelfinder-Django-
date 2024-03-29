# Generated by Django 2.0.1 on 2019-08-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelAdmin', '0006_auto_20190416_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image1',
            new_name='hostel_image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image2',
            new_name='kitchen',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image3',
            new_name='room',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='additional',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.AddField(
            model_name='hostel',
            name='additional_location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='district',
            field=models.CharField(default='Kathmandu', max_length=250),
        ),
        migrations.AddField(
            model_name='room',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fee',
            name='admission_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fee',
            name='refundable_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fee',
            name='security_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_type',
            field=models.CharField(choices=[('G', 'Girls Hostel'), ('B', 'Boys Hostel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip',
            field=models.CharField(default='44600', max_length=250),
        ),
    ]
