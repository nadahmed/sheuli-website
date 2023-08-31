from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create admin username and password"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)

    def handle(self, *args, **options):
        from django.contrib.auth.models import User

        username = options["username"]
        password = options["password"]

        if User.objects.filter(username=username).exists():
            raise CommandError("User already exists")

        User.objects.create_superuser(username=username, password=password, email="")
        self.stdout.write(self.style.SUCCESS("Admin user created"))    
