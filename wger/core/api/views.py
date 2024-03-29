# -*- coding: utf-8 -*-

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
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from wger.core.models import (
    UserProfile,
    Language,
    DaysOfWeek,
    License,
    RepetitionUnit,
    WeightUnit)
from wger.core.api.serializers import (
    UsernameSerializer,
    LanguageSerializer,
    DaysOfWeekSerializer,
    LicenseSerializer,
    RepetitionUnitSerializer,
    WeightUnitSerializer,
    UserprofileSerializer,
    UserApiSerializer
)
from wger.utils.permissions import UpdateOnlyPermission, WgerPermission


class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for workout objects
    '''
    is_private = True
    serializer_class = UserprofileSerializer
    permission_classes = (WgerPermission, UpdateOnlyPermission)
    ordering_fields = '__all__'

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return UserProfile.objects.filter(user=self.request.user)

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(User, 'user')]

    @detail_route()
    def username(self, request, pk):
        '''
        Return the username
        '''

        user = self.get_object().user
        return Response(UsernameSerializer(user).data)


class UserApiRegistrationViewset(viewsets.ModelViewSet):
    '''
    API endpoint for the created user from the external app.
    '''
    is_private = True
    serializer_class = UserApiSerializer
    ordering_fields = ('username', 'email', 'password')

    def get_queryset(self):
        '''
        Allow access to appropriate user.
        '''
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        profile = UserProfile.objects.get(user=user)
        profile.add_user_rest_api = True
        print(request.user.username)
        if UserProfile.objects.get(user=request.user).add_user_rest_api:
            serializer = UserApiSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            new_profile = User.objects.get(
                username=request.data.get('username'))
            new_profile.set_password(request.data.get('password'))
            new_profile.save()

            profile = UserProfile.objects.get(user=new_profile)
            profile.created_by = request.user.username
            profile.save()

            return Response({'Message': 'Profile created'}, status=status.HTTP_201_CREATED)
        return Response(
            {'Message': 'You Have no permission to add users.'}, status=status.HTTP_403_FORBIDDEN)


class ListApiUserProfileViewset(viewsets.ModelViewSet):
    '''
    Lists users created by the created user
    from the external app to avoid his usersaving
    to register  access wger instance.
    '''
    is_private = True
    serializer_class = UserprofileSerializer
    ordering_fields = ('username', 'email', 'password')

    def get_queryset(self):
        return UserProfile.objects.filter(created_by=self.request.user.username)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    ordering_fields = '__all__'
    filter_fields = ('full_name',
                     'short_name')


class DaysOfWeekViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
    ordering_fields = '__all__'
    filter_fields = ('day_of_week', )


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    ordering_fields = '__all__'
    filter_fields = ('full_name',
                     'short_name',
                     'url')


class RepetitionUnitViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for repetition units objects
    '''
    queryset = RepetitionUnit.objects.all()
    serializer_class = RepetitionUnitSerializer
    ordering_fields = '__all__'
    filter_fields = ('name', )


class WeightUnitViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for weight units objects
    '''
    queryset = WeightUnit.objects.all()
    serializer_class = WeightUnitSerializer
    ordering_fields = '__all__'
    filter_fields = ('name', )
