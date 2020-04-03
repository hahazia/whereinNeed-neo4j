from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from myapp.models import Charity, Categ
from pytz import UTC



CATEG_NAMES = [
    'Human Services',
    'Arts, Culture, Humanities',
    'Health',
    'Education',
    'International',
    'Religion',
    'Animals',
    'Community Development',
    'Environment',
    'Human and Civil Rights',
    'Research and Public Policy'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the charity data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from charity_data.csv into our Charity model"

    def handle(self, *args, **options):
        if Categ.objects.exists() or Charity.objects.exists():
            print('Charity data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating category data")
        for categ_name in CATEG_NAMES:
            categ = Categ(name=categ_name)
            categ.save()
        print("Loading charity data for charities available for donation")
        for row in DictReader(open('./charity_data.csv')):
            charity = Charity()
            charity.name = row['charityName']
            charity.webURL = row['\ufeffwebsiteURL']
            charity.mission = row['mission']
            charity.ein = row['ein']
            charity.rating = row['rating']
            charity.city = row['city']
            charity.zipCode = row['postalCode']
            charity.addr = row['streetAddress']
            charity.save()
            category_names = row['category']
            categ_names = [name.strip() for name in category_names.split('|') if name]
            for cat_name in categ_names:
                cat = Categ.objects.get(name=cat_name)
                charity.category.add(cat)
            charity.save()
