from unittest2 import TestCase

from api import GovTrackClient


class GovTrackAPITests(TestCase):
    def setUp(self):
        self.client = GovTrackClient()

    def tearDown(self):
        pass

    def test_url_encode_params(self):
        # encoding an int returns the string of that int
        test_params = 123
        self.assertEqual(self.client._url_encode_params(test_params), str(test_params))

        # encoding a dict without an 'id' key returns a query parameter string starting with a '?'
        test_params = {'var': 123}
        self.assertEqual(self.client._url_encode_params(test_params), '?var=123')

        # encoding a dict with an 'id' key returns a query parameter string prepended by the string of the 'id' value
        test_params = {'id': 65, 'var': 123}
        self.assertEqual(self.client._url_encode_params(test_params), '65?var=123')

    def test_bill(self):
        TEST_BILL_ID = 256509

        response = self.client.bill({'id': TEST_BILL_ID})

        self.assertTrue('id' in response and response['id'] == TEST_BILL_ID)
        self.assertTrue('number' in response and 'title' in response)

        TEST_CONGRESS_NUMBER = 113

        response = self.client.bill({'congress': TEST_CONGRESS_NUMBER})

        self.assertGreater(len(response), 0)

        self.assertTrue(response['objects'][0]['congress'] == TEST_CONGRESS_NUMBER)
        self.assertTrue('bill_type' in response['objects'][0])

    def test_cosponsorship(self):
        TEST_COSPONSORSHIP_ID = 1

        response = self.client.cosponsorship({'id': TEST_COSPONSORSHIP_ID})

        self.assertTrue('id' in response and response['id'] == TEST_COSPONSORSHIP_ID)
        self.assertTrue('bill' in response and 'person' in response)

    def test_person(self):
        TEST_PERSON_ID = 300001

        response = self.client.person({'id': TEST_PERSON_ID})

        self.assertTrue('id' in response and response['id'] == TEST_PERSON_ID)
        self.assertTrue('name' in response and 'roles' in response)

        TEST_LAST_NAME = 'Kennedy'

        response = self.client.person({'lastname': TEST_LAST_NAME})

        self.assertEqual(response['objects'][0]['lastname'], TEST_LAST_NAME)

    def test_role(self):
        TEST_ROLE_ID = 1

        response = self.client.role({'id': TEST_ROLE_ID})

        self.assertTrue('id' in response and response['id'] == TEST_ROLE_ID)
        self.assertTrue('role_type' in response and 'startdate' in response and 'person' in response)

    def test_vote(self):
        TEST_VOTE_ID = 67617

        response = self.client.vote({'id': TEST_VOTE_ID})

        self.assertTrue('id' in response and response['id'] == TEST_VOTE_ID)
        self.assertTrue('category' in response and 'chamber' in response and 'congress' in response and 'result' in response)

    def test_vote_voter(self):
        TEST_VOTE_VOTER_ID = 28927519

        response = self.client.vote_voter({'id': TEST_VOTE_VOTER_ID})

        self.assertTrue('id' in response and response['id'] == TEST_VOTE_VOTER_ID)
        self.assertTrue('person' in response and 'vote' in response and 'voter_type' in response)
