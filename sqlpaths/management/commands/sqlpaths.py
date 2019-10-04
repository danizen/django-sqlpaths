from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'sqlpaths management command(s)'

    def handle_status(self, subcmd, **kwargs):
        print('{} - not yet implemented'.format(subcmd))

    def handle_migrate(self, subcmd, **kwargs):
        print('{} - not yet implemented'.format(subcmd))

    def handle_validate(self, subcmd, **kwargs):
        print('{} - not yet implemented'.format(subcmd))

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(title='sub-command', dest='subcmd')
        
        status = subparsers.add_parser('status', help='Obtain status of path migrations')
        status.set_defaults(method=self.handle_status)

        migrate = subparsers.add_parser('migrate', help='Run path migrations without migrate')
        migrate.set_defaults(method=self.handle_migrate)

        validate = subparsers.add_parser('validate', help='Validate path migrations')
        validate.set_defaults(method=self.handle_validate)

    def handle(self, method, **kwargs):
    	method(**kwargs)
