from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from myapp.models import User,Profile
from pytz import UTC

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the user data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from users.csv into user data"

    def handle(self, *args, **options):
        if User.objects.exists():
            print('User data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        
        print("Creating user data")
        for row in DictReader(open('./users.csv')):
            try:
                user = User.objects.create_user(username=row['UserName'],password=row['Pin'])
                user.save()
            except:
                continue

        print("Creating user's profile data")
        for row in DictReader(open('./users.csv')):
            profile=Profile()
            a=User.objects.get(username=row['UserName'])
            if not a.profile.city :
                a.profile.date_joined = row['DateJoined']
                a.profile.city = row['City']
                a.profile.save()
            else:
                continue
            