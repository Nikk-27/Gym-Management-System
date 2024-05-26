
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_enquiry_equipment_member_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='planname',
            new_name='name',
        ),
    ]
