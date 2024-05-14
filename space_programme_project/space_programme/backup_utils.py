import os
from django.core.management import call_command
from django.conf import settings


def backup_database():
    backup_folder = settings.DBBACKUP_STORAGE_OPTIONS['location']
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    filename = os.path.join(backup_folder, 'backup_db.sql')
    call_command('dbbackup', '--output', filename)