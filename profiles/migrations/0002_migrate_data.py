"""
Migration to transfer data from oc_lettings_site to profiles app.
"""
from django.db import migrations


def transfer_profiles_data(apps, schema_editor):
    """Transfer Profile data from oc_lettings_site to profiles app."""
    # Get models from both apps
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    
    # Transfer Profile data
    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )


def reverse_transfer(apps, schema_editor):
    """Reverse the data transfer."""
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):
    
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]
    
    operations = [
        migrations.RunPython(transfer_profiles_data, reverse_transfer),
    ]