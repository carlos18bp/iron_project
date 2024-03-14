from django.core.management.base import BaseCommand
from faker import Faker
from iron.models import User

class Command(BaseCommand):
    help = 'Create user records in the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int, nargs='?', default=10)

    def handle(self, *args, **options):
        number_of_users = options['number_of_users']
        fake = Faker()  

        for _ in range(number_of_users):
            new_user = User.objects.create(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                contact = fake.random_int(min=3000000000, max=3030000000),
            )

            self.stdout.write(self.style.SUCCESS(f'user "{new_user}" created'))
        
        print(f'"{len(User.objects.all())}" user records created')