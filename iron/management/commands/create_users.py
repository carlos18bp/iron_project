from django.core.management.base import BaseCommand
import random
from faker import Faker
from iron.models import User

class Command(BaseCommand):
    help = 'Create user records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_users = options['number_of_users']
        fake = Faker()
        project_options = ['Balconies',
                               'Doors',
                               'Fences',
                               'Furniture',
                               'Gates',
                               'Home Decor',
                               'Lighting']
        
        profession_options = ['Home Owner',
                      'Designer',
                      'Architect',
                      'Contractor',
                      'Other']
        
        hear_about_us_options = ['Web page',
                         'Instagram',
                         'Friend',
                         'Internet']

        for _ in range(number_of_users):
            new_user = User.objects.create(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                contact = fake.random_int(min=3000000000, max=3030000000),
                subject = fake.word(),
                description  = fake.text(max_nb_chars=400),
                projects = random.sample(project_options, random.randint(1, len(project_options)-1)),
                professions = random.sample(profession_options, random.randint(1, len(profession_options)-1)),
                hear_about_us = random.choice(hear_about_us_options)
            )

            self.stdout.write(self.style.SUCCESS(f'user "{new_user}" created'))
        
        print(f'"{len(User.objects.all())}" user records created')