
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_rename_planname_plan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
