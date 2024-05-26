
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('age', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('purchasedate', models.DateField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('gender', models.DateField(max_length=10, null=True)),
                ('plan', models.CharField(max_length=100, null=True)),
                ('joindate', models.DateField(null=True)),
                ('initamount', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planname', models.CharField(max_length=150, null=True)),
                ('amount', models.CharField(max_length=15, null=True)),
                ('duration', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
