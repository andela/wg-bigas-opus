# -*- coding: utf-8 *-*

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from wger.core.models import UserProfile


class Command(BaseCommand):
    '''
    Administrator uses this command to allow an user
    with external app to be able to add user via REST API
    '''
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '--disable',
            action='store_true',
            dest='disable',
            default=False,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        #
        try:
            user = User.objects.get(username=options['username'])
            profile = UserProfile.objects.get(user=user)
            if options['disable']:
                profile.add_user_rest_api = False
            else:
                profile.add_user_rest_api = True
                profile.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        "{0} can now add users via the rest api".format(
                            options['username']
                        )
                    )
                )
        except Exception as ex:
            self.stdout.write(self.style.WARNING(ex))
