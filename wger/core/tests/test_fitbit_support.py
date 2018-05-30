import os
import urllib
from django.core.urlresolvers import reverse
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from django.conf import settings
import requests
import json
from wger.core.views.fitbit import FitBit


class IntegrateWithFitbitTestCase(WorkoutManagerTestCase):

    """
    Test Integration with fitbit
    """
    # Import environment variables

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    SCOPE = os.environ.get('SCOPE')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    AUTHORIZE_URI = os.environ.get('AUTHORIZE_URI')

    # Set parameters

    params = {
            'client_id': CLIENT_ID,
            'response_type': 'code',
            'scope': SCOPE,
            'redirect_uri': REDIRECT_URI
    }

    def test_it_shows_instructions(self):
        """
        Test if the link received is the actual link required
        """
        # encode the parameters
        urlparams = urllib.parse.urlencode(self.params)
        # construct and return authorization_uri
        url = str(self.AUTHORIZE_URI) + "?" + str(urlparams)
        self.user_login()
        r = self.client.get(reverse('core:fitbit-login'))
        status_code = r.status_code
        self.assertRedirects(r, url, status_code=302, target_status_code=200,
        msg_prefix='', fetch_redirect_response=False)

    def test_app_redirects_to_fitbit(self):
        """
        Test if link redirects ti the site
        """
        self.user_login()
        r = self.client.get(reverse('core:fitbit-login'))
        status_code = r.status_code
        self.assertEqual(r.status_code, 302)

   