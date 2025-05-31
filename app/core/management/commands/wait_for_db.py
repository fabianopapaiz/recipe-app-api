"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2_OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')

        db_up = False
        
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (Psycopg2_OpError, OperationalError):
                self.stdout.write('Database unavailable, wainting 1 second to try again...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))

        return super().handle(*args, **options)()