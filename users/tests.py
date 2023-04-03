# from django.test import TestCase
# from django.urls import reverse
# from django.utils.timezone import now
# from http import HTTPStatus
# from .models import User, EmailVerification
#
# from datetime import timedelta
#
#
# class UserRegistrationViewTestCase(TestCase):
#
#     def setUp(self):
#         self.path = reverse('users:registration')
#         self.data = {
#             'first_name': 'Peter', 'last_name': 'Parker',
#             'username': 'parker', 'email': 'parker@gmail.com',
#             'password1': '12345678Qw', 'password2': '12345678Qw',
#         }
#
#     def test_user_registration_get(self):
#         response = self.client.get(self.path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response.context_data['title'], 'Store - Registration')
#         self.assertTemplateUsed(response, 'users/registration.html')
#
#     def test_user_registration_post_success(self):
#         username = self.data['username']
#         self.assertFalse(User.objects.filter(username=username).exists())
#         response = self.client.post(self.path, self.data)
#
#         # check creating of user
#         self.assertEqual(response.status_code, HTTPStatus.FOUND)
#         self.assertRedirects(response, reverse('users:login'))
#         self.assertTrue(User.objects.filter(username=username).exists())
#
#         # check creating of email verification
#         email_verification = EmailVerification.objects.filter(user__username=username)
#         self.assertTrue(email_verification.exists())
#         self.assertEqual(
#             email_verification.first().expiration.date()
#             (now() + timedelta(minutes=15)).date()
#         )
#
#     def test_user_registration_post_error(self):
#         User.objects.create(username=self.data['username'])
#         response = self.client.post(self.path, self.data)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertContains(response, 'A user with that username already exists.', html=True)