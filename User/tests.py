from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from User.models import User
from rest_framework.test import force_authenticate

email = 'admin@test.com'
password = 'mypassword'
admin = None
user1 = None
class UserTests(APITestCase):
    def test_create_account_no_auth(self):
        """
        Ensure we cannot create user when not logged in.
        """
        url = reverse('user-list')
        data = {'name': 'user name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(User.objects.count(), 0)
        # self.assertEqual(User.objects.get().name, 'DabApps')

    def test_signup_and_login_as_admin(self):
        """
        Ensure we can login as admin.
        """
        Admin = User.objects.create_superuser('admin', email, password)
        self.assertEqual(User.objects.count(), 1)
        self.client.login(email = email, password = password)



    # def test_create_account(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('user-list')
    #     data = {'email': 'asdasd'}
    #     self.client.force_authenticate(user = admin)
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # self.assertEqual(Account.objects.count(), 1)
    #     # self.assertEqual(Account.objects.get().name, 'DabApps')