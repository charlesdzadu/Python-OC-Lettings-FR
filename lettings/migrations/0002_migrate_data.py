"""
Migration to transfer data from oc_lettings_site to lettings app.
"""
from django.db import migrations


def transfer_lettings_data(apps, schema_editor):
    """Transfer Address and Letting data from oc_lettings_site to lettings app."""
    # Get models from both apps
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    
    # Transfer Address data
    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
    
    # Transfer Letting data
    for old_letting in OldLetting.objects.all():
        new_address = NewAddress.objects.get(id=old_letting.address.id)
        NewLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address=new_address
        )


def reverse_transfer(apps, schema_editor):
    """Reverse the data transfer."""
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    
    NewLetting.objects.all().delete()
    NewAddress.objects.all().delete()


class Migration(migrations.Migration):
    
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(transfer_lettings_data, reverse_transfer),
    ]