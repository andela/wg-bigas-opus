from wger.core.tests.base_testcase import WorkoutManagerTestCase


class ExerciseInfoTestCase(WorkoutManagerTestCase):
    '''
    Test the Exercise Info endpoint
    '''

    def test_exercise_info_endpoint(self):
        '''
        Test that the endpoint returns all exercise infomation
        '''
        endpoint = "/api/v2/exercisedetails/"

        resp = self.client.get(endpoint)

        self.assertEqual(resp.status_code, 200)

        self.assertIn("license_author", str(resp.data))

        self.assertIn("uuid", str(resp.data))

        self.assertIn("license", str(resp.data))

        self.assertIn("category", str(resp.data))

        self.assertIn("language", str(resp.data))

        self.assertIn("muscles", str(resp.data))

        self.assertIn("muscles_secondary", str(resp.data))

        self.assertIn("equipment", str(resp.data))